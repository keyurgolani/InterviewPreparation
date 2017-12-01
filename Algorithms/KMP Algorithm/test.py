import app


def test_solution():
    assert not app.KMP.search("aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaab")
    assert app.KMP.search("alsdkfsadfghsdfkj", "ghs")
    assert not app.KMP.search("asldsdlfjfshdfsdkjfshfafkadjfhasdfkasdjfashdf",
                              "sdlfsdfh")
    assert app.KMP.search(
        "adsfkajsdfashdfasdskdjsdfgasfasdfkasjdfhasdfaskdfjashdfadfkasjdfhas" +
        "dflasdfjashdfasdlkfj", "ash")
