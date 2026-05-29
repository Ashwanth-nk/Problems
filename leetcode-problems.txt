'''
# Hard
# 3093. Longest Common Suffix (Hard)
# 800+ Testcases ran (Dint pass 9)
# Error: Time Limit Executed
wordsContainer = ["abcd","bcd","xbcd"]
wordsQuery = ["cd","bcd","xyz"]
ans = []
for i in wordsQuery:
    x = []
    for j in wordsContainer:
        a = 0
        c = min(len(i) - 1, len(j) - 1)
        m, n = len(i) - 1, len(j) - 1
        while c > -1:
            if j[n] == i[m]:
                a += 1
                c -= 1
                m -= 1
                n -= 1
            else:
                break
        if a > 0:
            if x == []:
                x.append([j, a])
            else:
                if a > x[0][1]:
                    x = [[j, a]]
                elif a == x[0][1] and len(j) < len(x[0][0]):
                    x = [[j, a]]
    if x != []:
        ans.append(wordsContainer.index(x[0][0]))
    else:
        ans.append(wordsContainer.index(sorted(wordsContainer, key=len)[0]))
print(ans)


// Easy
// 58. Length of Last Word
// 100% Runtime, 45% Memory
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let u = s.trim().split(/\s+/);
    return u[u.length-1].length;
};


// Easy
// 28. Find the Index of the First Occurrence in a String
// 100% Runtime, 67% Memory
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if (haystack.length < needle.length){
        return -1
    }
    let i = 0;
    let j = needle.length;
    let c = 0;
    while (j<haystack.length+1){
        if (haystack.slice(i,j) === needle) {
            return c
        }
        i++
        j++
        c++
    }
    return -1
};


// Easy
// 3300. Minimum Element After Replacement With Digit Sum
// 76% Runtime, 63% Memory
/**
 * @param {number[]} nums
 * @return {number}
 */
var minElement = function(nums) {
    let least = null;
    for (let i = 0; i<nums.length; i++) {
        let ans = 0;
        a = nums[i];
        while (a>0){
            ans+=(a%10)
            a = Math.floor(a/10)
        }
        if (least === null){
            least = ans
        } else if (ans < least){
            least = ans
        }
    }
    return least;
};
'''