from src.core import generate_pairs


def test_generate_pairs():
    """
    Test that generate_pairs returns a dict of pairs with
    no person being gifted more than once
    and no person gifting more than one person
    and no gifter gifting themselves
    """

    people = ["a", "b", "c", "d", "e"]
    pairs = generate_pairs(people)
    print(pairs)
    assert len(pairs) == len(people)
    assert len(set(pairs.values())) == len(people)
    assert len(set(pairs.keys())) == len(people)
    for person in people:
        assert pairs[person] != person
