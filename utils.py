class Utils:

    def reversed(in_num: int) -> int:
        assert type(in_num) == int, "Input is not a 'int' type"
        
        new_num = int(str(in_num)[::-1])
        return new_num

    def formatter(in_num: int) -> str:
        assert type(in_num) == int, "Input is not a 'int' type"
        return bin(in_num), oct(in_num)
