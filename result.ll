@n = common global i32 0, align 4
@temp = common global i32 0, align 4

define void @fact(i32 %n) {
    %1 = icmp sle i32 %n, 1
    br i1 %1, label %L1, label %L2
    L1:
    store i32 1, i32* @temp, align 4
    br label %L3
    L2:
    %2 = sub nsw i32 %n, 1
    call void @fact(i32 %2)
    %3 = load i32, i32* @temp, align 4
    %4 = mul nsw i32 %3, %n
    store i32 %4, i32* @temp, align 4
    br label %L3
    L3:
    ret void
    ret void
}

define i32 @main() {
    %1 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* @n)
    %2 = load i32, i32* @n, align 4
    call void @fact(i32 %2)
    %3 = load i32, i32* @temp, align 4
    %4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %3)
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
declare i32 @scanf(i8*, ...)
@.str.r = private unnamed_addr constant [3 x i8] c"%d\00", align 1
