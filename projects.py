class Post:
	def __init__(self,img,postt,timer,desc,link=None):
		self.icon = img
		self.title = postt
		self.date = timer
		self.description = desc
		self.url = link

def makePosts(postfile):
	f = open(postfile, 'r')
	numPosts = int(f.readline().strip())
	posts = []
	for n in range(numPosts):
		img = f.readline().strip()
		postt = f.readline().strip()
		timer = f.readline().strip()
		desc = ""
		link = ''
		descl = f.readline().strip()
		while descl not in ("#","!"):
			desc+=descl = "\n"
			descl = f.readline()
		if descl == "!":
			link = f.readline().strip()
		posts.append(Post(img,postt,timer,desc,link))
	return posts