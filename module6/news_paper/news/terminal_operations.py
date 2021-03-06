# весь код ниже вбивался через терминал, что-то закомментирванно, чтобы имитировать вывод консоли или там,
# где IDE ругается, мол, statement has no affect


from news.models import *

User.objects.create_user('Юрий')
User.objects.create_user('Толян')
yuri = User.objects.get(pk=1)  # к юзерам и авторам обращаться точно будем, поэтому сразу заключим их в переменные
tolyan = User.objects.get(pk=2)

auth_yuri = Author.objects.create(user=yuri)
auth_tolyan = Author.objects.create(user=tolyan)

cat_sport = Category.objects.create(name='Спорт')
cat_policy = Category.objects.create(name='Политика')
cat_economy = Category.objects.create(name='Экономика')
cat_countryside = Category.objects.create(name='Советы для дачников')

# для создания постов весь текст сначала распихиваем по переменным, чтобы не перегружать одну команду массой текста
# пока я думал над update_rating набросал статьи. Как вы можете видеть, с юмором у меня так себе, надеюсь с
# программированием сложится лучше)
art_title_togo = 'Ситуация на африканском рынке украшений близка к катастрофической'
art_text_togo = 'В Того на фоне санкций со стороны Ганы резко подорожали ожерелья из крокодильих зубов,' \
                ' что вызвало массовые протесты со стороны Африканской Ассоциации Жен Племенных Вождей (ААЖПВ). ' \
                'Напомним, что конфликт между странами разгорелся на фоне обвинений верховного шамана Ганы в том, ' \
                'что жители Того "Слишком активно молятся, привлекая на свои земли слишком много дождей,' \
                ' которых не получают соседние страны, в частности Гана". В то же время в Гане местные ' \
                'производители ожерелий бьют тревогу, так как "на их фермах без дела стареют сотни крокодилов".' \
                ' Напомним, продажа украшений из зубов приносила Гане до 93% ВВП'
art_title_beer = 'Как преуспеть в беге за пивом на короткие дистанции'
art_text_beer = 'Многие из нас уже успели освоить любительский уровень такой безусловно самой популярной и самой ' \
                'народной олимпийской дисциплины, как бег за пивом. Однако существует множество разных факторов,' \
                ' которые мешают продвинуться дальше, открыть для себя новые грани данного спорта и возможно даже ' \
                'выйти на настоящий олимпийский уровень. Мы подготовили для вас несколько советов, которые помогут' \
                ' из приятного увлечения сделать бег за пивом смыслом всей жизни. 1) Расширьте для себя географию' \
                ' ларьков. Успешные спортсмены отмечают, что верный путь для того, чтобы избежать стагнации - ' \
                'открывать для себя новые точки с разливным. "Только пробуя новое можно сохранить в себе страсть' \
                ' для будущих рекордов" - отмечает авторитетное спортивное издание spirts.ru. 2) Приобретите теще' \
                ' дачный участок подальше от вашего места тренировок. Наличие отвлекающих и раздражающих факторов' \
                ' крайне негативно влияет на спортивные результаты, что ещё в 69 году до н.э заметил величайший' \
                ' философ Джейсон Стетхэм. Постарайтесь организовать вокруг себя атмосферу, максимально' \
                ' благоприятствующую процессу тренировок. 3) Привлекайте подрастающее поколение. Таким образом вы' \
                ' не только повысите собственную заинтересованность в процессе, но и сможете вырастить достойную' \
                ' смену, которая, возможно, сможет покорить те спортивные вершины, которых не смогли достичь вы'
art_title_mole = 'Способы прогнать крота, не привлекая внимания санитаров'
art_text_mole = 'Вопросом того, как прогнать крота с участка озаботились еще древние египтяне, ведь для того,' \
                ' чтобы строить пирамиды нужна была крепкая почва для фундамента. Как мы сегодня можем видеть, ' \
                'у них получилось, ну а наша задача: проанализировать методы, которыми они пользовались. ' \
                '1) Громко слушайте шансон. Стоит помнить, что поскольку крот слеп, у него хорошо развит слух, а ' \
                'судя по его прекрасной чёрной шубе, он так же не обделён и вкусом, поэтому вы можете быть уверены,' \
                ' что совокупность этих качеств не позволят ему долго вас выносить, если вы будете громко включать' \
                ' хиты таких классиков жанра как «бутырка» и Михаил Круг, и крот вынужден будет ретироваться. Вместе' \
                ' с адекватными соседями. 2) Предложите кроту вложиться в пирамиду. Крот либо сразу вынужден будет' \
                ' уйти, либо, если он ещё молод и наивен, он уйдёт после, как поймёт, что его обманули. 3) Внушите' \
                ' кроту, что он пожилой президент, а на дворе конец 99-го, и он точно уйдёт, ведь он устал и вообще' \
                ' он Мухожук.'
# так куда красивее и лаконичнее
post_togo = Post.objects.create(author=auth_yuri, type='News', title=art_title_togo, content=art_text_togo)
post_beer = Post.objects.create(author=auth_tolyan, type='Articles', title=art_title_beer, content=art_text_beer)
post_mole = Post.objects.create(author=auth_tolyan, type='Articles', title=art_title_mole, content=art_text_mole)

PostCategory.objects.create(posts=post_togo, categories=cat_policy)
PostCategory.objects.create(posts=post_togo, categories=cat_economy)
PostCategory.objects.create(posts=post_beer, categories=cat_sport)
PostCategory.objects.create(posts=post_mole, categories=cat_countryside)

# как и с постами, не перегружаем команды текстом
comm1_text = 'Ганский шаман-то нормальный дядька, а в Того одни каннибалы, особенно в правительстве. Слава Гане!!!'
comm2_text = 'Да и вообще, есть проблемы посерьёзнее! Я вон отправил тещу в тульскую область на дачу, а у нее там ' \
             'кроты весь участок перекопали так, что дом на 1,5м в землю ушёл, она и приехала обратно, мол она не ' \
             'крот и в отличие от них под землей жить не может. Ещё и сын оболтус вместо того чтобы спортом ' \
             'заниматься как отец сидит целый день сайты клепает на этом вашем Жанхо... А вы со своим Того совсем... ' \
             'того!'
comm3_text = 'На короткие дистанции — это всё для маменькиных сынков. Настоящие мужики на дальние дистанции' \
             ' перемещаются. По болотам и лесам, на уазах! И не за пивом, а за чем покрепче. Хотя мой уаз уже' \
             ' старичок — ему 4 месяца и он только с 5го раза заводится. Чувствую скоро я к вашей братии примкну.'
comm4_text = 'У меня дед петардой кротов пытался прогнать, ну мол, в норку кинуть, чтоб их там оглушило и они' \
             ' поразбегались все. Вот только с размерами петарды прогадал. Теперь на месте его дачи водохранилище.'

comm1 = Comment.objects.create(author=tolyan, related_post=post_togo, text=comm1_text)
comm2 = Comment.objects.create(author=tolyan, related_post=post_togo, text=comm2_text)
comm3 = Comment.objects.create(author=yuri, related_post=post_beer, text=comm3_text)
comm4 = Comment.objects.create(author=yuri, related_post=post_mole, text=comm4_text)

# предположим, что Африканские проблемы не произвели впечатления на читателей, да и кроты оказались куда более
# настойчивыми, а вот возможность заняться спортом, совместив приятное с полезным, народ оценил
post_togo.dislike()
post_beer.like()
post_mole.dislike()

# политические лозунги Толяна поддержаны не были, зато в остальном мнения сошлись
comm1.dislike()
comm2.like()
comm3.like()
comm4.like()

# отсюда имеем следующую ситуацию с рейтингами
auth_yuri.update_rating()
# auth_yuri.rating
# -1
auth_tolyan.update_rating()
# auth_tolyan.rating
# 2
# а вот тут я как раз и столкнулся с проблемой вывода юсернейма через прямое обращение к классу Author
# если не успел исправить на момент проверки, обещаю, изучу документацию и найду решение
top = Author.objects.all().order_by('-rating').first()
# top.user.username
# 'Толян'
# top.rating
# 2
Author.objects.all().order_by('-rating').values('user', 'rating').first()
# {'user': 2, 'rating': 2} # зато это поле ссылается на User.pk Не слишком показательно, согласен

top_art = Post.objects.all().order_by('-rating').values('publishing_date', 'rating', 'title').first()
# top_art
# {'publishing_date': datetime.datetime(2022, 4, 29, 22, 35, 55, 489944),
# 'rating': 1, 'title': 'Как преуспеть в беге за пивом на короткие дистанции'}
# Post.objects.all().order_by('-rating').first().author.user.username
# 'Толян'
# Post.objects.all().order_by('-rating').first().preview()
# 'Многие из нас уже успели освоить любительский уровень такой
# безусловно самой популярной и самой народной олимпийской дисципл...'

top_post = Post.objects.all().order_by('-rating').first()
Comment.objects.all().filter(related_post=top_post).values('author', 'text', 'publishing_date', 'rating')
# <QuerySet [{'author': 1, 'text': 'На короткие дистанции — это всё для маменькиных сынков. Настоящие мужики на
# дальние дистанции перемещаются. По болотам и лесам, на уаз
# ах! И не за пивом, а за чем покрепче. Хотя мой уаз уже старичок — ему 4 месяца
# и он только с 5го раза заводится. Чувствую скоро я к вашей братии примкну.', 'publishing_
# date': datetime.datetime(2022, 4, 29, 22, 56, 52, 540899), 'rating': 1}]>

