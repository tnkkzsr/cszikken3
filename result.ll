@x = common global i32 0, align 4

define i32 @main() {
    %1 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* @x)
    %2 = load i32, i32* @x, align 4
    %3 = icmp slt i32 %2, 0
    br i1 %3, label %L1, label %L2
    L1:
    %4 = load i32, i32* @x, align 4
    %5 = sub nsw i32 0, %4
    store i32 %5, i32* @x, align 4
    br label %L3
    L2:
    br label %L3
    L3:
    %6 = load i32, i32* @x, align 4
    %7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %6)
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
declare i32 @scanf(i8*, ...)
@.str.r = private unnamed_addr constant [3 x i8] c"%d\00", align 1
