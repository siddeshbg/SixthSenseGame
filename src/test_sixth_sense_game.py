import SixthSenseGame


def test_box_count():
    boxes = SixthSenseGame.Boxes()
    assert 6 == len(boxes.box)

def test_all_boxes_are_initiaized():
    boxes = SixthSenseGame.Boxes()
    boxes.initialize()
    for x in range(6):
        assert boxes.box[x] != 0

def test_all_boxes_contains_unique_value():
    boxes = SixthSenseGame.Boxes()
    boxes.initialize()

    values = set()
    for x in range(6):
        print("Box %s = %s" % (x, boxes.box[x]), end=' ')
        values.add(boxes.box[x])

    assert 6 == len(values)
