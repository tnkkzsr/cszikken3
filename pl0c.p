program PL0C;
var n, res;
procedure fact();
var m, temp;
begin
    if n <= 1 then
        temp := 1
    else
    begin
        m := n;
        n := n-1;
        fact();
        temp := res * m
    end;
    res := temp
end;
begin
    read(n);
    fact();
    write(res)
end.
