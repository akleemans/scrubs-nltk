from __future__ import division
import nltk

"""
Script with some examples for using NLTK (http://www.nltk.org/).
Don't run this all at once, this is more of a collection than an executable script.
"""

with open('all_subtitles_clean.txt', 'r') as read_file:
    data = read_file.read()

print 'Number of characters:', len(data)
print 'Number of screens:', len(data.split('\n'))

data = data.decode("ascii", "ignore").encode("ascii")

tokens = nltk.word_tokenize(data)
text = nltk.Text(tokens)

### similarity and context ###

# similar words
text.similar('surgeon') # doctor, guy, hospital, second, kid, man
text.similar('football') # outside, baseball, golf
text.similar('freedom') # sleep, coffee, practice, sunny
text.similar('vascular') # arterial, heart, surgical, plastic, pulmonary

# common context
text.common_contexts(['Kelso', 'Cox']) # tell_that, what_said, because_has, dr_will, dr_did, sorry_i, to_office
text.common_contexts(['love', 'hate']) # i_cox
text.common_contexts(['black', 'white']) # big_ass, a_girl, a_doctor

# show surroundings
text.concordance('patient') # basic keyword-in-context
"""
.. Could you drop an NG tube on the patient in 234 and then call the attending
n yesterday did n't really focus on patient care . The hospital does n't wan na
 a mistake , do n't admit it to the patient . Of course , if the patient is dec
to the patient . Of course , if the patient is deceased , and you 're sure , yo
ll me what to look for in a uraemic patient . Anyway , I 'm going for it . Infe
c insufficiency . That 's my girl . Patient number two . `` Superior mesenteric
 has to run the room , decides if a patient lives or dies . What , am I crazy ?
end to remember your names . If the patient has insurance , you treat them . If
 It 's a piece of cake . It 's your patient . You 're leaving ? That 's your pa
nt . You 're leaving ? That 's your patient , doctor . Good . That 's enough .
 She forgot to check the stats on a patient and gave me attitude . Did you tell
 new . Look , man . You 're a great patient . I like you enough to hope I never
se . That was a great catch on that patient with meningococcus . That actually
Severe swelling of the lips in this patient might be an indication of what ? An
"""

text.concordance('Jackman')
"""
scovered dimensions . Oh ! And Hugh Jackman . Hugh Jackman 's Wolverine ! How d
ions . Oh ! And Hugh Jackman . Hugh Jackman 's Wolverine ! How dare he . I miss
ays , we 're not that big on Hugues Jackman . Look here . The only thing men ac
 tolerant of everyone . Except Hugh Jackman . Huh . I do n't understand why you
at I might finally happen upon Hugh Jackman and give him the present I 've been
free ice-creams , crack baby , Hugh Jackman and cancer all happenin ' for a rea
ar , a sequel to Hope Floats , Hugh Jackman winning an oscar ... Yeah , yeah ,
 but I liked it . Does he like Hugh Jackman ? Wrong again . You suck at this .
as I 'll ignore the opening of Hugh Jackman 's next cinematic excretion . Jorda
mention is , and of course ... Hugh Jackman ! Hugh Jackman ! That was nice , I
d of course ... Hugh Jackman ! Hugh Jackman ! That was nice , I liked that . We
"""

text.concordance('Kelso')
"""
 apartment . OK , gang , I 'm Dr Bob Kelso , and I 'm your Chief of Medicine ,
romise our no-talking agreement . Dr Kelso is always saying ... I 'm gon na say
ible , so I do n't overstate it . Dr Kelso is the most evil human being on the
all need lots of things . Great . Dr Kelso ? You 're the Chief of Medicine . Is
 . Carla , I should n't have told Dr Kelso on you . No , you should n't have .
 the big spoon or the little spoon ? Kelso did n't ask her , she gave you full
go hang out in your room ? I know Dr Kelso does n't mean anything by it , and O
n na do . Go down there and confront Kelso . Really ? Absolutely . Never mind t
do with you . I had a run-in with Dr Kelso , so when he switched me to you , I
naugh today ? Yes . Yes , I did . Dr Kelso , I just wanted to say , well , as f
Dr Cox sat behind me . Sending me to Kelso like that , I 'm not sure what you w
How fun was that ? Just initial . Dr Kelso . I wonder if you could give me your
 sneaky , Death . Hope I helped . Dr Kelso came down on you , huh ? Yeah , but
he ladies . You 're the one who told Kelso that Mr Martinez was dead ? That 's
"""

text.concordance('JD', lines=100) # show other than default 25 lines
text.concordance('scrubs', 50) # change left and right context width to 10 characters and show all results
text.concordance('disease')
text.concordance('cancer')
text.concordance('janitor', 40, lines=10)

### frequency ###

print len(text) # 704583 tokens
print len(set(text)) # 24626 unique numbers of tokens
print text.count('Bambi') # count specific token - 72

sorted(set(text))[:50] # sorted set

# lexical diversity
print len(set(text)) / len(text) # number of distinct words is just 3.5% of the total number of words

# calculate word length
lengths = {}
for word in text:
    l = len(word)
    if l in lengths: lengths[l] += 1
    else: lengths[l] = 1
    if l > 25: print word # longest words

# longest words
long_words = [w for w in text if len(w) > 25]
print long_words

'''
Whatever-the-hell-your-name-is
two-hours-after-his-shift-
Too-Scared-To-Get-ln-The-Game
Esophogeo-gastro-duodeno-colitis
bring-your-problems-to-work
Yesterday-l-Had-Chest-Hair
block-the-door-with-my-foot
Rin-Tin-Tin-Tin-Tin-Tin-Tin
you-leaving-the-room-whenever-I-enter-it
everandeverandeverandeveraneverandever
Aaaaaaaaaaaaaaagggggggggggggggggghhhhhhhhhhhhhhhhhhhh
aaagghhh-hagh-haaaaggghhhh
Noooooooooooooooooooooooooooooooooooooooooooooo
Riiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiight
daaaaaaaiiiiiioooooooowwww
Buddy-buddy-buddy-buddy-buddy
What's-He-Over-Compensating-For
tickletickletickletickletickle
...
'''

# sentences TODO average length per sentence
# 77k sentences
sents = nltk.sent_tokenize(data)
print 'Number of sentences:', len(sents)
print 'Average length of sentence:', len(data)/len(sents)
print 'Average nr. of words per sentence:', len(text)/len(sents)

"""
>>> print 'Number of sentences:', len(sents)
Number of sentences: 76821
>>> print 'Average length of sentence:', len(data)/len(sents)
Average length of sentence: 37.1235859986
>>> print 'Average nr. of words per sentence:', len(text)/len(sents)
Average nr. of words per sentence: 9.11080303563
"""

# basic frequency
fd = nltk.FreqDist(text) # creates a new data object that contains information about word frequency
fd['the'] # how many occurences of the word �the�
fd.items()[0:50] # just show a portion of the info.

fd['disease']
fd.freq('disease') # %
fd.N()

### clean text even more! ###

# 1. de-capitalize
text_nostop = [w.lower() for w in text]

# 2. remove interpunctuation
interp = ['.', ',', '?', '!', ':', ';', '"', "'", '$', '#', '``', "''", '(', ')', '--']
text_nostop = [w for w in text_nostop if w not in interp]

# 3. remove stopwords
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
my_stopwords = ["'s", "n't", '...', "'m", "'re", "'ll", 'gon', "'ve", "'d", 'na', 'yeah', 'ca', 'ta', 'wo']

# from http://www.lextek.com/manuals/onix/stopwords2.html
with open('additional_stopwords.txt', 'r') as read_file:
    buckley_salton = read_file.read()

additional_stopwords = buckley_salton.split('\n')
print 'additional_stopwords:', additional_stopwords

text_nostop = [w for w in text_nostop if w not in (stopwords + my_stopwords + additional_stopwords)]

# -> unique tokens, or count, or word cloud plot without stopwords

# new distribution
fd_nostop = nltk.FreqDist(text_nostop)

# most common words without stopwords!
for w, f in fd_nostop.most_common(100):
    print w + ':' + str(f)

"""
hey:1418
time:1231
good:1216
turk:1126
back:1103
dr.:1087
make:914
baby:857
thing:846
elliot:808
god:803
people:801
love:796
man:732
guy:723
jd:711
carla:698
cox:650
great:631
guys:630
talk:622
day:622
doctor:617
give:597
hell:574
dr:573
work:571
patient:528
feel:523
things:507
"""

fd_nostop.plot(30, cumulative=False)


"""
[('know', 3575), ('like', 2795), ('get', 2539), ('oh', 2301), ('na', 2218), ('go
t', 2025), ('go', 1961), ('right', 1934), ('one', 1900), ('think', 1535), ('yeah
', 1433), ('hey', 1418), ('see', 1330), ('would', 1308), ('want', 1299), ('look'
, 1296), ('well', 1258), ('could', 1247), ('really', 1242), ('time', 1231), ('go
od', 1216), ('turk', 1126), ('say', 1123), ('come', 1118), ('ca', 1116), ('let',
 1108), ('back', 1103), ('dr.', 1087), ('tell', 1048), ('little', 1008), ('going
', 983), ('make', 914), ('even', 873), ('baby', 857), ('take', 854), ('never', 8
50), ('thing', 846), ('way', 844), ('okay', 832), ('need', 829), ('elliot', 808)
, ('god', 803), ('people', 801), ('love', 796), ('man', 732), ('still', 725), ('
guy', 723), ('ok', 713), ('jd', 711), ('sorry', 709), ('carla', 698), ('somethin
g', 694), ('mean', 654), ('cox', 650), ('us', 639), ('great', 631), ('guys', 630
), ('--', 623), ('talk', 622), ('day', 622), ('doctor', 617), ('much', 607), ('s
aid', 604), ('give', 597), ('two', 592), ('sure', 584), ('yes', 579), ('hell', 5
74), ('dr', 573), ('work', 571), ('help', 561), ('first', 560), ('new', 557), ('
last', 554), ('actually', 535), ('ever', 535), ('always', 531), ('around', 528),
 ('patient', 528), ('feel', 523), ('thank', 517), ('maybe', 516), ('things', 507
), ('please', 507), ('every', 497), ('life', 482), ('someone', 480), ('stop', 46
7), ('big', 464), ('kelso', 454), ('call', 451), ('thought', 451), ('hospital',
449), ('mr.', 444), ('ta', 435), ('fine', 426), ('night', 415), ('put', 415), ('
uh', 412), ('told', 404)]

Names: Turk (winner!), Elliot, JD, Kelso, Carla
Other name: Dr., doctor, guy, mr., someone
"""

# dispersion plot
text.dispersion_plot(['Kelso','Cox']) # different patterns
text.dispersion_plot(['JD','Carla','Turk']) # Carla fading in the end
text.dispersion_plot(['Bambi', 'Newbie']) # Bambi: strong in the beginning, fades away. Same with newbie, but holds far longer!
text.dispersion_plot(['Dr', 'Doc', 'Doctor'])
text.dispersion_plot(['god', 'religion', 'faith', 'hope'])

# chunking, collocations ("quick glimpse what text is about")
text_nostop = nltk.Text(text_nostop)

text_nostop.collocations()
"""
dr. cox; even though; last night; dr. kelso; sacred heart; dr. reid;
looks like; med school; high school; big deal; chief medicine; best
friend; feel like; little bit; mrs. wilk; every time; take care; cell
phone; dr. dorian; every day; john dorian; dr. turk; bob kelso; make
sure; last time; god sake; superman superman; number one; getting
married; bottom line; years ago; blah blah; med student; one thing;
fair enough; chief resident; brain trust; tid tid; someone else; bink
bink; last week; good news; beg pardon; surgical consult; ten minutes;
look like; hey guys; residency director; gum gum; nurse roberts; rest
life; leave alone; test results; good luck; first time; private
practice; good morning; could help; ice cream; thank god; brown bear;
let see; six months; ever since; every single; nah nah; whatever want;
cup coffee; hugh jackman; come back; sounds like; holy cow; med
students; give break; train wreck; came back; pretty much; snoop dogg;
ladies gentlemen; five minutes; two weeks; say something; supply
closet; acting like; good night; kick ass; dear god; let get; parking
lot; whoa whoa; shortness breath; nurse espinosa; mr. corman; whole
thing; central line; mr. foster; dr. mahoney; need help; bad news;

- Doctors, chief medicine
- Hospital, Sacred Heart
- John Dorian
- best friend
- "Superman, superman" => intro song
- med school, med student
- blah blah
- "hey guys"-phrase
- normal collocations: cell phone, bottom line, fair enough, leave alone, good morning
"""

text_nostop.collocations(num=100) # alter nr of phrases returned


### Advanced usage ###

# find most frequent trigrams
trigrams = {}
for trigram in nltk.trigrams(text):
    if trigram in trigrams: trigrams[trigram] += 1
    else: trigrams[trigram] = 1

print 'Most common trigrams:', '\n'.join([' '.join(t) for t in trigrams if trigrams[t] > 400])
"""
Most common trigrams:
. It 's
. Oh ,
I ca n't
do n't know
. Well ,
I 'm gon
. You know
. You 're
. I do
I 'm not
? I 'm
. Yeah ,
I do n't
, it 's
. Hey ,
. I 'm
, you 're
. That 's
, I 'm
'm gon na
"""

# POS tagging - cool, this works!
nltk.pos_tag(text[:100])
"""
[('I', 'PRP'), ("'ve", 'VBP'), ('always', 'RB'), ('been', 'VBN'), ('able', 'JJ')
, ('to', 'TO'), ('sleep', 'VB'), ('through', 'IN'), ('anything', 'NN'), ('.', '.
'), ('Storms', 'NNP'), (',', ','), ('sirens', 'VBZ'), (',', ','), ('you', 'PRP')
, ('name', 'VBP'), ('it', 'PRP'), ('.', '.'), ('Last', 'JJ'), ('night', 'NN'), (
',', ','), ('I', 'PRP'), ('did', 'VBD'), ("n't", 'RB'), ('sleep', 'VB'), ('.', '
.'), ('I', 'PRP'), ('guess', 'VBP'), ('I', 'PRP'), ('get', 'VBP'), ('a', 'DT'),
('little', 'JJ'), ('goofy', 'NN'), ('when', 'WRB'), ('I', 'PRP'), ("'m", 'VBP'),
 ('nervous', 'JJ'), ('.', '.'), ('You', 'PRP'), ('see', 'VBP'), (',', ','), ('to
day', 'NN'), ('is', 'VBZ'), ("n't", 'RB'), ('just', 'RB'), ('any', 'DT'), ('othe
r', 'JJ'), ('day', 'NN'), ('.', '.'), ('It', 'PRP'), ("'s", 'VBZ'), ('my', 'PRP$
'), ('first', 'JJ'), ('day', 'NN'), ('.', '.'), ('I', 'PRP'), ("'m", 'VBP'), ('t
he', 'DT'), ('man', 'NN'), ('.', '.'), ('Three', 'CD'), ('years', 'NNS'), ('of',
 'IN'), ('pre-med', 'JJ'), ('and', 'CC'), ('four', 'CD'), ('years', 'NNS'), ('of
', 'IN'), ('med', 'JJ'), ('school', 'NN'), ('have', 'VBP'), ('made', 'VBN'), ('m
e', 'PRP'), ('realise', 'VB'), ('one', 'CD'), ('thing', 'NN'), ('...', ':'), ('C
ould', 'NNP'), ('you', 'PRP'), ('drop', 'VBP'), ('an', 'DT'), ('NG', 'NNP'), ('t
ube', 'NN'), ('on', 'IN'), ('the', 'DT'), ('patient', 'NN'), ('in', 'IN'), ('234
', 'CD'), ('and', 'CC'), ('then', 'RB'), ('call', 'VB'), ('the', 'DT'), ('attend
ing', 'NN'), ('?', '.'), ('...', ':'), ('I', 'PRP'), ('do', 'VBP'), ("n't", 'RB'
), ('know', 'VB'), ('Jack', 'NNP')]
"""

# defining a grammar

from nltk.parse.generate import generate, demo_grammar
from nltk import CFG

mygrammar = nltk.CFG.fromstring("""
 S  -> NP VP
 Nom -> Adj Nom | N
 VP -> VP VP | VP PP | V Adj | V NP | V S | V NP PP
 PP -> Prep V | Prep Adj
 V    -> 'have' | 'been' | 'sleep'
 NP   -> 'I'
 Adj  -> 'always' | 'anything' | 'able'
 Prep -> 'to' | 'through'
 """)

sentence = "I have always been able to sleep through anything".split(' ')
parser = nltk.ChartParser(mygrammar)
for tree in parser.parse(sentence):
	print(tree)
"""
(S
  (NP I)
  (VP
    (VP (V have) (Adj always))
    (VP
      (VP (VP (V been) (Adj able)) (PP (Prep to) (V sleep)))
      (PP (Prep through) (Adj anything)))))
(S
  (NP I)
  (VP
    (VP
      (VP (VP (V have) (Adj always)) (VP (V been) (Adj able)))
      (PP (Prep to) (V sleep)))
    (PP (Prep through) (Adj anything))))
(S
  (NP I)
  (VP
    (VP
      (VP (V have) (Adj always))
      (VP (VP (V been) (Adj able)) (PP (Prep to) (V sleep))))
    (PP (Prep through) (Adj anything))))
"""

# draw first tree
from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

cf = CanvasFrame()
t = Tree.fromstring("(S (NP I) (VP (VP (V have) (Adj always)) (VP (VP (VP (V been) (Adj able)) (PP (Prep to) (V sleep))) (PP (Prep through) (Adj anything)))))")
tc = TreeWidget(cf.canvas(),t)
cf.add_widget(tc, 10, 10)
#cf.print_to_file('tree.ps') # save to file
cf.destroy()
