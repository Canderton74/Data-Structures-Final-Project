import bisect

class data_container:
	def __init__(self,id,values):
		self.id=id
		self.values=values
	def __eq__(self,other):
		return True if self.id==other.id else False
	def __ne__(self,other):
		return False if self.id!=other.id else True
	def __lt__(self,other):
		return True if self.id<other.id else False
	def __gt__(self,other):
		return True if self.id>other.id else False
	def __le__(self,other):
		return True if self.id<=other.id else False
	def __ge__(self,other):
		return True if self.id>=other.id else False

class node:
	def __init__(self,n,m,data,children,next_node,parent):
		self.n=n
		self.m=m
		self.data=data
		self.next_node=next_node
		self.parent=parent
		self.children=children
	def insert(self,value):
		bisect.insort(self.data,value)
		if(len(self.data)>=self.m):
			split()
	def split(self):
		new_node=node(n,m,data[len(data)//2:],children[len(children)//2:],next_node,parent)
		next_node=new_node
		data=data[:len(values)//2]
		children=children[:len(children)//2]
		if(parent==None):
			parent=node(n,m,[],[self,next_node],None,None)
		parent.push_up(new_node,values[len(values)//2+1])
	def push_up(self,new_node,value):
		insert(value)
		children[bisect.bisect_left(children,value)]=new_node
		if(len(children)>=n):
			split()

class b_plus_tree:
	def __init__(self,n,m):
		self.n=n
		self.m=m
		self.leaves=[]
		self.empty=True
		self.total=0
		self.total_cities=0
		self.root=node(self.n,self.m,[],[],None,None)
	def insert(self,data):
		if(isinstance(data,str)):
			data=data_container(data,0)
		current_node=self.root
		while(current_node.children):
			current_node=current_node.children[bisect.bisect_left(current_node.children,data)]
		self.total+=1
		if(current_node.data!=[]):
			for value in current_node.data:
				if(value == data):
					value.values+=1
		else:
			current_node.insert(data)
		self.total_cities+=1
	def search(self,data):
		if(isinstance(data,str)):
			data=data_container(data,0)
		current_node=self.root
		while(current_node.children):
			current_node=current_node.children[bisect.bisect_left(current_node.children,data)]
		if(current_node.data):
			for value in current_node.data:
				if(value == data):
					return value.values
		else:
			return 0
	def get_tree_height(self):
		current_node=self.root
		height=0
		while(current_node.children):
			current_node=current_node.children[bisect.bisect_left(current_node.children,data)]
			height+=1
		return height

def main():
    cities = ["New York", "Los Angeles", "Chicago", "New York", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington", "Boston", "El Paso", "Detroit", "Nashville", "Portland", "Memphis", "Oklahoma City", "Las Vegas", "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Mesa", "Kansas City", "Atlanta", "Omaha", "Colorado Springs", "Raleigh", "Miami", "Long Beach", "Virginia Beach", "Oakland", "Minneapolis", "Tulsa", "Tampa", "Arlington"]

    # Initialize Red-Black Tree
    tree = b_plus_tree(2,3)

# Insert cities into the Red-Black Tree
    for city in cities:
        tree.insert(city)
    
    print(tree.total)
    print(tree.total_cities)
# Print the tree
    #tree.print_tree()
    print(tree.get_tree_height())
    print(len(cities))

    print(tree.search("New York"))

main()