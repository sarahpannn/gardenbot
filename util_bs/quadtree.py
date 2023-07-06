import math


class QuadTreeNode:
    def __init__(self, region):
        self.region = region
        self.objects = []
        self.children = [None, None, None, None]

class QuadTree:
    def __init__(self, boundary, max_objects_per_node):
        self.root = QuadTreeNode(boundary)
        self.max_objects_per_node = max_objects_per_node

    def insert(self, obj):
        self._insert_recursive(self.root, obj)

    def _insert_recursive(self, node, obj):
        if not self._intersects_region(node.region, obj):
            return

        node.objects.append(obj)

        if len(node.objects) > self.max_objects_per_node:
            if not any(node.children):
                self._subdivide(node)

            for child in node.children:
                self._insert_recursive(child, obj)

    def _intersects_region(self, region, obj):
        xmin, ymin, xmax, ymax = region
        x, y, radius = obj.center_x, obj.center_y, obj.radius

        dx = max(xmin - x, 0, x - xmax)
        dy = max(ymin - y, 0, y - ymax)
        return dx*dx + dy*dy <= radius*radius

    def _subdivide(self, node):
        xmin, ymin, xmax, ymax = node.region
        xmid = (xmin + xmax) / 2
        ymid = (ymin + ymax) / 2

        node.children[0] = QuadTreeNode((xmid, ymid, xmax, ymax))
        node.children[1] = QuadTreeNode((xmin, ymid, xmid, ymax))
        node.children[2] = QuadTreeNode((xmin, ymin, xmid, ymid))
        node.children[3] = QuadTreeNode((xmid, ymin, xmax, ymid))

        for child in node.children:
            for obj in node.objects:
                self._insert_recursive(child, obj)
        node.objects = []

    def calculate_overlap(self, obj1, obj2):
        overlap = 0.0
        self._calculate_overlap_recursive(self.root, obj1, obj2, overlap)
        return overlap

    def _calculate_overlap_recursive(self, node, obj1, obj2, overlap):
        if not self._intersects_region(node.region, obj1) or not self._intersects_region(node.region, obj2):
            return

        for obj in node.objects:
            if self._objects_overlap(obj, obj1) and self._objects_overlap(obj, obj2):
                overlap += self._calculate_circle_overlap(obj, obj1, obj2)

        for child in node.children:
            if child:
                overlap = self._calculate_overlap_recursive(child, obj1, obj2, overlap)

        return overlap

    def _objects_overlap(self, obj1, obj2):
        distance = math.sqrt((obj1.center_x - obj2.center_x)**2 + (obj1.center_y - obj2.center_y)**2)
        return distance < obj1.radius + obj2.radius