(read_char)
.
[
    >
    [-]
    +
    >
    [-]
    <<
    (subtract/right)
    [
        (add/right)
        (subtract/double_quote)
        [
            (add/double_quote)
            (subtract/single_quote)
            [
                (add/single_quote)
                (subtract/hash)
                [
                    (add/hash)
                    (subtract/slash)
                    [
                        (add/slash)
                        (subtract/space)
                        [
                            (add/space)
                            (subtract/newline)
                            [
                                (add/newline)
                                >
                                (read_char)
                                .
                                >
                            ]
                            >
                            [
                                -
                                <
                                (syntax/newline)
                                >>
                            ]
                            <
                        ]
                        >
                        [
                            -
                            <
                            (syntax/space)
                            >>
                        ]
                        <
                    ]
                    >
                    [
                        -
                        <
                        (syntax/slash)
                        >>
                    ]
                    <
                ]
                >
                [
                    -
                    <
                    (syntax/hash)
                    >>
                ]
                <
            ]
            >
            [
                -
                <
                (syntax/single_quote)
                >>
            ]
            <
        ]
        >
        [
            -
            <
            (syntax/double_quote)
            >>
        ]
        <
    ]
    >
    [
        -
        <
        (syntax/right) 15
        >>
    ]
    <<
]
