from PyInquirer import style_from_dict, Token

custom_style = style_from_dict(
    {
        Token.Separator: "#000000 bold",
        Token.Selected: "#FFFFFF bold italic",
        Token.Pointer: "#28FE14 bold",
        Token.Instruction: "#FFFFFF",
        Token.Answer: "#28FE14",
        Token.Question: "#BD93F9 bold",
    }
)