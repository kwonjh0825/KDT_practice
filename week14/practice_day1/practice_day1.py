# 할일 Model & ORM

# 1. 아래 할 일 생성
Todo.objects.create(content='실습 제출', priority=5, deadline='2023-3-28')

# 2. 아래 할 일 생성
Todo.objects.create(content='데일리 설문(오후) 제출', deadline='2023-3-28')

# 3. 임의의 할 일 5개 생성
Todo.objects.create(content='프로그래머스 문제 풀기', priority=4, deadline='2023-3-28')
Todo.objects.create(content='TIL 작성', priority=4, deadline='2023-3-28')
Todo.objects.create(content='TIL 업로드', priority=4, deadline='2023-3-28')
Todo.objects.create(content='오후 실습 복기', priority=4, deadline='2023-3-28')
Todo.objects.create(content='퇴실 체크', priority=5, deadline='2023-3-28')

# 4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
Todo.objects.order_by('pk')

# 5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
Todo.objects.order_by('-priority')

# 6. pk가 1인 단일 데이터의 아래 필드 조회
# (pk, content, priority, deadline, created_at) 
Todo.objects.values('pk','content', 'priority', 'deadline', 'created_at').get(pk=1)

# 신문 Model & ORM

# 1. pk 필드가 1인 단일 데이터의 journalist 필드 조회
Newspaper.objects.get(pk=1).journalist

# 2. journalist 필드가 Laney Mcculough 인 데이터 개수 조회
Newspaper.objects.filter(journalist='Laney Mccullough').count()

# 3. pk 필드 기준 내림차순으로 정렬한 모든 데이터 조회
Newspaper.objects.order_by('-pk')

# 4. created_at 필드 기준 내림차순으로 정렬한 모든 데이터 조회
Newspaper.objects.order_by('-created_at')

# 5. journalist 필드가 Britney를 포함하는 데이터 개수 조회
Newspaper.objects.filter(journalist__contains='Britney').count()

# 6. journalist 필드가 ['Britney Mahoney', 'Arianna Walls', 'Carl Short']에 속하는 데이터 개수 조회
Newspaper.objects.filter(journalist__in=['Britney Mahoney', 'Arianna Walls', 'Carl Short']).count()

# 7. created_at 필드가 2000-01-01 이후 데이터 개수 조회
Newspaper.objects.filter(created_at__gt='2000-01-01').count()

# 8. 마지막 단일 데이터의 title, content,  jounalist 필드 조회 
a = Newspaper.objects.order_by('-pk')[0]
print(f'title : {a.title}')
print(f'content : {a.content}')
print(f'journalist : {a.journalist}')