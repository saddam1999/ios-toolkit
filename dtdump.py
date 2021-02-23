from ctypes import Structure, c_char, c_uint32, sizeof
from argparse import ArgumentParser
from pprint import pprint


class NodePropertyHeader(Structure):
    _pack_ = 1
    _fields_ = [
        ('name', c_char * 32),
        ('size', c_uint32)
        # Value of variable length follows immediately after
    ]


class NodeHeader(Structure):
    _pack_ = 1
    _fields_ = [
        ('property_count', c_uint32),
        ('children_count', c_uint32)
        # Properties follow after
        # Children follow after
    ]


class Node:
    PROPERTY_ALIGNMENT = 4

    def __init__(self, blob):
        self._header = NodeHeader.from_buffer_copy(blob)
        position = sizeof(NodeHeader)

        self._properties = {}
        for i in range(self._header.property_count):
            property_header = NodePropertyHeader.from_buffer_copy(blob[position:])
            position += sizeof(NodePropertyHeader)
            self._properties[property_header.name] = blob[position:position + property_header.size]
            position += property_header.size
            if position % self.PROPERTY_ALIGNMENT:
                position += self.PROPERTY_ALIGNMENT - (position % self.PROPERTY_ALIGNMENT)

        self._children = []
        for i in range(self._header.children_count):
            child = Node(blob[position:])
            position += child._size
            self._children.append(child)

        self._size = position
        assert len(self._properties) == self._header.property_count, "Unexpected property count!"
        assert len(self._children) == self._header.children_count, "Unexpect children count!"

    @property
    def properties(self):
        return self._properties

    @property
    def children(self):
        return self._children


def print_node(node):
    print('Properties:')
    pprint(node.properties)
    i = 0
    for child in node.children:
        print('Child {}'.format(i))
        print_node(child)
        i += 1


def build_parser():
    parser = ArgumentParser(description='Small utility to dump decrypted iOS device trees')
    parser.add_argument('blob', help='decrypted devicetree blob extracted from im4p file')
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    with open(args.blob, 'rb') as dtb_file:
        content = dtb_file.read()
    node = Node(content)
    print_node(node)


if __name__ == '__main__':
    main()
