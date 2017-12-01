import app


def test_solution():
    assert not app.solution("aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaab")
    assert app.solution("alsdkfsadfghsdfkj", "ghs")
    assert not app.solution("asldsdlfjfshdfsdkjfshfafkadjfhasdfkasdjfashdf",
                            "sdlfsdfh")
    assert app.solution(
        "adsfkajsdfashdfasdskdjsdfgasfasdfkasjdfhasdfaskdfjashdfadfkasjdfhas" +
        "dflasdfjashdfasdlkfj", "ash")
