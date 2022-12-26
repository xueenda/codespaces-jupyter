tests = [
    {
        "name": "TestSum",
        "des": "Test Sum",
        "assert": lotto.test_sum,
        "rule": "rank",
        "column": "SumNoBonus",
        "rank": show_column_rank(df, "SumNoBonus")
    },
    {
        "name": "TestPrev",
        "desc": "Test with Previous 6 Draws",
        "assert": lotto.test_count_in_prev_draws,
        "rule": "rank",
        "column": "Prev6",
        "rank": show_column_rank(df, "Prev6")
    },
    {
        "name": "TestOnesDigit",
        "desc": "Test Ones Digit",
        "assert": lotto.test_ones_digit,
        "rule": "rank",
        "column": "OnesDigit",
        "rank": show_column_rank(df, "OnesDigit")
    },
    {
        "name": "TestTensDigit",
        "desc": "Test Tens Digit",
        "assert": lotto.test_tens_digit,
        "rule": "rank",
        "column": "TensDigit",
        "rank": show_column_rank(df, "TensDigit")
    },
    {
        "name": "TestBigSmall",
        "desc": "Test Big Small Nums",
        "assert": lotto.test_big_small,
        "rule": "rank",
        "column": "BigSmall",
        "rank": show_column_rank(df, "BigSmall")
    },
    {
        "name": "TestPrime",
        "desc": "Test Prime Numbers",
        "assert": lotto.test_prime,
        "rule": "rank",
        "column": "Prime",
        "rank": show_column_rank(df, "Prime")
    },
    {
        "name": "TestMinPrimeSum",
        "desc": "Test Sum of Min Prime Numbers",
        "assert": lotto.test_min_prime_sum,
        "rule": "rank",
        "column": "MinPrimeSum",
        "rank": show_column_rank(df, "MinPrimeSum")
    },
    {
        "name": "TestAC",
        "desc": "Test AC Value",
        "assert": lotto.test_ac_value,
        "rule": "rank",
        "column": "AC",
        "rank": show_column_rank(df, "AC")
    },
    {
        "name": "TestDivide2",
        "desc": "Test Divide by 2",
        "assert": lotto.test_divide(2),
        "rule": "rank",
        "column": "Divide2",
        "rank": show_column_rank(df, "Divide2"),
    },
    {
        "name": "TestDivide3",
        "desc": "Test Divide by 3",
        "assert": lotto.test_divide(3),
        "rule": "rank",
        "column": "Divide3",
        "rank": show_column_rank(df, "Divide3"),
    },
    {
        "name": "TestDivide5",
        "desc": "Test Divide by 5",
        "assert": lotto.test_divide(5),
        "rule": "rank",
        "column": "Divide5",
        "rank": show_column_rank(df, "Divide5"),
    },
]