@n = common global i32 0, align 4
@res = common global i32 0, align 4

define void @fact() {
    %m = alloca i32, align 4
    %temp = alloca i32, align 4
    %1 = load i32, i32* @n, align 4
    %2 = icmp sle i32 %1, 1
    br i1 %2, label %L1, label %L2
    L1:
    store i32 1, i32* %temp, align 4
    br label %L3
    L2:
    %3 = load i32, i32* @n, align 4
    store i32 %3, i32* %m, align 4
    %4 = load i32, i32* @n, align 4
    %5 = sub nsw i32 %4, 1
    store i32 %5, i32* @n, align 4
    call void @fact()
    %6 = load i32, i32* @res, align 4
    %7 = load i32, i32* %m, align 4
    %8 = mul nsw i32 %6, %7
    store i32 %8, i32* %temp, align 4
    br label %L3
    L3:
    %9 = load i32, i32* %temp, align 4
    store i32 %9, i32* @res, align 4
    ret void
}

define i32 @main() {
    %1 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* @n)
    call void @fact()
    %2 = load i32, i32* @res, align 4
    %3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %2)
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
declare i32 @scanf(i8*, ...)
@.str.r = private unnamed_addr constant [3 x i8] c"%d\00", align 1
