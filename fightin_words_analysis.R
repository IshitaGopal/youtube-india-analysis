#setwd('/Users/gopali/Library/CloudStorage/Box-Box/Projects/youtube-india-analysis/')

source("FW_function.R")
library(quanteda)

ytTitles <- read.csv('data/yt_channel_vids_combined.csv')
ytTitles$party <- factor(ytTitles$party)

# Create a corpus
ytTitles.corpus <- corpus(ytTitles, text_field = "translated_text")

# Tokenize the corpus
ytTitles.tokens <- tokens(ytTitles.corpus, 
                          remove_punct = TRUE,
                          remove_symbols = TRUE) %>%
  tokens_wordstem(language = "english")

# Create a Document-Feature Matrix (DFM)
ytTitles.dfm <- dfm(ytTitles.tokens) %>%
  dfm_remove(stopwords("english"))
ytTitles.dfm <- dfm_trim(ytTitles.dfm, min_docfreq = 10)
dim(ytTitles.dfm)

fw.titleparty <- fwgroups(ytTitles.dfm, groups = ytTitles$party)

fwkeys.titles <- fw.keys(fw.titleparty, n.keys=50)

p.fw.titleparty <- fw.ggplot.groups(fw.titleparty,sizescale=2.2,max.words=50,max.countrank=400,colorpalette=c("darkorange2","blue"))
p.fw.titleparty

