def lengthOfLongestSubstring(s):
    """
    Given a string, find the length of the longest substring without repeating
     characters.
     O(n) Time complexity
     O(n) Memory
    :param s:
    :return:
    """
    dicSeq = {}
    maxCount = 0
    tempCount = 0
    lastIndex = 0
    for i, ch in enumerate(s):
        if ch in dicSeq and dicSeq[ch] >= lastIndex:
            if tempCount > maxCount:  # checking length of sublist
                maxCount = tempCount
            lastIndex = dicSeq[ch]
            tempCount = i - lastIndex
            dicSeq[ch] = i
        else:
            tempCount += 1
            dicSeq[ch] = i
    return max(maxCount, tempCount)
