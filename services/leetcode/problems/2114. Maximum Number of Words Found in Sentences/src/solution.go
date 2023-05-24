package src

import "strings"

func mostWordsFound(sentences []string) (maxWordCount int) {
    for _, sentence := range sentences {
        wordCount := strings.Count(sentence, " ") + 1

        if maxWordCount < wordCount {
            maxWordCount = wordCount
        }
    }

    return
}
