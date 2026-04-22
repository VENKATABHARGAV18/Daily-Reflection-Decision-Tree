import csv

# Load TSV into dictionary (id → node)
def load_tree(file):
    tree = {}
    with open(file, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            tree[row['id']] = row
    return tree

# Get next node based on parentId
def find_next(tree, current):
    for node in tree.values():
        if node['parentId'] == current:
            return node['id']
    return None

def run_agent(tree):
    current = "START"
    answers = {}

    while True:
        node = tree.get(current)

        if not node:
            print("Error: Node not found")
            break

        node_type = node['type']
        text = node['text']

        # Start node
        if node_type == 'start':
            print(text)
            current = find_next(tree, current)

        # Question node (takes user input)
        elif node_type == 'question':
            print(text)

            options = node['options'].split('|')
            for i, opt in enumerate(options):
                print(str(i+1) + ". " + opt)

            try:
                choice = int(input("Choose option: ")) - 1
                if choice < 0 or choice >= len(options):
                    print("Invalid choice")
                    continue
            except:
                print("Enter number only")
                continue

            answers[node['id']] = options[choice]
            current = find_next(tree, current)

        # Decision node (maps answer → next node)
        elif node_type == 'decision':
            parent = node['parentId']
            user_answer = answers.get(parent, "")

            rules = node['target'].split(';')

            for rule in rules:
                if ':' not in rule:
                    continue

                condition, target = rule.split(':', 1)
                condition = condition.replace("answer=", "")

                if user_answer in condition:
                    current = target
                    break
            else:
                current = find_next(tree, current)

        # Reflection node (prints insight)
        elif node_type == 'reflection':
            print(text)
            current = find_next(tree, current)

        # Bridge node (moves to next axis)
        elif node_type == 'bridge':
            print(text)
            current = node['target']

        # Summary node
        elif node_type == 'summary':
            print(text)
            current = "END"

        # End node
        elif node_type == 'end':
            print(text)
            break

        else:
            print("Unknown node type")
            break

if __name__ == "__main__":
    tree = load_tree("reflection-tree.tsv")
    run_agent(tree)