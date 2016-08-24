library(wordcloud)
library(tm)

oc <- c("#5C6E00", "#273B00", "#F7DA00", "#EB1200", "#F78200")

# set directory to contain text file(s)
t <- Corpus(DirSource(directory = ".", encoding="utf-8"), readerControl = list(language = "eng"))
mycorpus <- tm_map(t, removePunctuation)
mycorpus <- tm_map(mycorpus, tolower)
mycorpus <- tm_map(mycorpus, function(x) removeWords(x, stopwords("english")))
mycorpus <- tm_map(mycorpus, PlainTextDocument)
tdm <- TermDocumentMatrix(mycorpus)

m <- as.matrix(tdm)
v <- sort(rowSums(m), decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
wordcloud(d$word,d$freq, scale=c(6,.5),min.freq=2, max.words=50, random.order=F, random.color=T, rot.per=.20, colors=oc)