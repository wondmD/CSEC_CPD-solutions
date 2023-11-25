class Solution:
    def compress(self, chars: List[str]) -> int:
        write_ptr = 0
        read_ptr = 0
        count = 0
        while read_ptr < len(chars):
            curr_char = chars[read_ptr]
            while read_ptr < len(chars) and chars[read_ptr] == curr_char:
                count += 1
                read_ptr += 1
            chars[write_ptr] = curr_char
            write_ptr += 1

            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write_ptr] = digit
                    write_ptr += 1
            count = 0

        return write_ptr