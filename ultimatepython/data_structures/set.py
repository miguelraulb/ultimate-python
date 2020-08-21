def main():
    # Define two `set` collections
    multiples_two = set()
    multiples_four = set()

    # Fill sensible values into the set using `add`
    for i in range(10):
        multiples_two.add(i * 2)
        multiples_four.add(i * 4)

    print("Multiples of two", multiples_two)
    print("Multiples of three", multiples_four)

    # One cannot decide in what order the numbers come out - so what
    # we're really looking for is fundamental truths like this one
    # which can be quite fascinating
    multiples_common = multiples_two.intersection(multiples_four)
    for number in multiples_common:
        assert number % 2 == 0 and number % 4 == 0

    print("Multiples in common", multiples_common)

    # You can compute exclusive multiples
    multiples_two_exclusive = multiples_two.difference(multiples_four)
    multiples_four_exclusive = multiples_four.difference(multiples_two)
    assert len(multiples_two_exclusive) and len(multiples_four_exclusive)

    # Numbers in this bracket are >2*9 and <4*10
    for number in multiples_four_exclusive:
        assert 18 < number < 40

    print("Exclusive multiples of two", multiples_two_exclusive)
    print("Exclusive multiples of four", multiples_four_exclusive)

    multiples_all = multiples_two.union(multiples_four)
    print("All multiples", multiples_all)

    # Check if set A is subset of set B
    assert multiples_four_exclusive.issubset(multiples_four)
    assert multiples_four.issubset(multiples_all)

    # Check that set A is subset and superset of itself
    assert multiples_all.issubset(multiples_all)
    assert multiples_all.issuperset(multiples_all)

    # Check if set A is superset of set B
    assert multiples_all.issuperset(multiples_two)
    assert multiples_two.issuperset(multiples_two_exclusive)


if __name__ == "__main__":
    main()
