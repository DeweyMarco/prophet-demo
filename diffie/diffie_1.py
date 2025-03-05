from __future__ import annotations


def find_primitive(modulus: int) -> int | None:
    """
    Find a primitive root modulo modulus, if one exists.

    Args:
        modulus : The modulus for which to find a primitive root.

    Returns:
        The primitive root if one exists, or None if there is none.
    """
    for r in range(1, modulus):
        li = []
        for x in range(modulus - 1):
            val = pow(r, x, modulus)
            if val in li:
                break
            li.append(val)
        else:
            return r
    return None
