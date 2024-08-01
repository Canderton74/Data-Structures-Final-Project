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
		self.compare_value=None if not data else data[0].id
		self.n=n
		self.m=m
		self.data=data
		self.next_node=next_node
		self.parent=parent
		self.children=children
		self.leaf=True if not self.children else False
	def insert(self,value):
		bisect.insort(self.data,value)
		self.compare_value=self.data[0].id
		if(not self.leaf and len(self.data)>self.n or self.leaf and len(self.data)>self.m):
			self.split()
	def split(self):
		print("leaf" if self.leaf else "internal", len(self.data),len(self.children))
		if(self.leaf):
			new_node=node(self.n,self.m,self.data[len(self.data)//2:],self.children[len(self.children)//2:],self.next_node,self.parent)
			self.next_node=new_node
			self.data=self.data[:len(self.data)//2]
			self.children=self.children[:len(self.children)//2]
			
			if(not self.parent):
				print("new root")
				self.parent=node(self.n,self.m,[new_node.data[0]],[self,self.next_node],None,None)
				new_node.parent=self.parent
			else:
				self.parent.push_up(new_node,new_node.data[0])

		else:
			self.next_node=node(self.n,self.m,self.data[-(len(self.data)//-2):],self.children[-(len(self.children)//-2):],self.next_node,self.parent)
			temp_datum=self.data[len(self.data)//2]
			self.data=self.data[:len(self.data)//2]
			self.children=self.children[:len(self.children)//2]
			if(not self.parent):
				print("new root")
				self.parent=node(self.n,self.m,[temp_datum],[self,self.next_node],None,None)
				self.next_node.parent=self.parent
			else:
				print("new parent")
				self.parent.push_up(self.next_node,temp_datum)
	def push_up(self,new_node,value):
		bisect.insort(self.children,new_node)
		for child in self.children:
			if(child):
				print(child.data[0].id)
		
		self.insert(value)
		
	def __eq__(self,other):
		return True if self.compare_value==other.compare_value else False
	def __ne__(self,other):
		return False if self.compare_value!=other.compare_value else True
	def __lt__(self,other):
		return True if self.compare_value<other.compare_value else False
	def __gt__(self,other):
		return True if self.compare_value>other.compare_value else False
	def __le__(self,other):
		return True if self.compare_value<=other.compare_value else False
	def __ge__(self,other):
		return True if self.compare_value>=other.compare_value else False
class b_plus_tree:
	#note: still not a b+ tree until leaves know they are leaves, such that n and m are used correctly
	def __init__(self,n,m):
		self.n=n
		self.m=m
		self.empty=True
		self.total=0
		self.total_cities=0
		self.root=node(self.n,self.m,[],[],None,None)
		self.first_leaf=self.root
	def insert(self,data):
		print("data",data)
		if(isinstance(data,str)):
			data=data_container(data.lower(),1)
		current_node=self.root
		while(current_node.children):
			print("children:", ' '.join(str(child.compare_value) for child in current_node.children))
			print("data:", ' '.join(str(datum.id) for datum in current_node.data))

			chosen_idx=bisect.bisect_left(current_node.data,data)
			print("bisect_left result:",chosen_idx)
			if(chosen_idx==len(current_node.children)):
				print("overflow?", ' '.join(str(child.id) for child in current_node.children[-1].data))

			current_node=current_node.children[chosen_idx]
		print("chosen:",current_node.compare_value)
		self.total+=1
		if(current_node.data):
			for value in current_node.data:
				if(value == data):
					
					value.values+=1
					print("incrementing", value.values)
					return
			current_node.insert(data)
		else:
			current_node.insert(data)
		while(self.root.parent):
			self.root=self.root.parent
		self.total_cities+=1
	def search(self,data):
		if(isinstance(data,str)):
			data=data_container(data.lower(),1)
		current_node=self.root
		while(current_node.children):
			print("children:", ' '.join(str(child.compare_value) for child in current_node.children))
			print("data:", ' '.join(str(datum.id) for datum in current_node.data))

			chosen_idx=bisect.bisect_left(current_node.data,data)
			print("bisect_left result:",chosen_idx)
			if(chosen_idx==len(current_node.children)):
				print("overflow?", ' '.join(str(child.id) for child in current_node.children[-1].data))

			current_node=current_node.children[chosen_idx]
		print("chosen:",current_node.compare_value)
		if(current_node.data):
			print("data:", ' '.join(str(datum.id) for datum in current_node.data))
			for value in current_node.data:
				if(value == data):
					return value.values
		else:
			print("somethign")
			return 0
	def get_tree_height(self):
		current_node=self.root
		height=0
		data=data_container("a",1)
		while(current_node.children):
			current_node=current_node.children[bisect.bisect_left(current_node.data,data)]
			height+=1
			# print(height)
		return 0 if height == 0 else height - 1
	def print_tree(self):
		current_node=self.first_leaf
		while(current_node.next_node):
			current_node=current_node.next_node
			for datum in current_node.data:
				print(datum.id)


def main():
    cities = ["New York", "Los Angeles", "Chicago", "New York", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington", "Boston", "El Paso", "Detroit", "Nashville", "Portland", "Memphis", "Oklahoma City", "Las Vegas", "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Mesa", "Kansas City", "Atlanta", "Omaha", "Colorado Springs", "Raleigh", "Miami", "Long Beach", "Virginia Beach", "Oakland", "Minneapolis", "Tulsa", "Tampa", "Arlington"]

    # Initialize Red-Black Tree
    tree = b_plus_tree(2,2)

# Insert cities into the Red-Black Tree
    for city in cities:
        tree.insert(city)
    
    print(tree.total)
    print(tree.total_cities)
# Print the tree
    tree.print_tree()
    print(tree.get_tree_height())
    print(len(cities))

    print(tree.search("New York"))

main()