from colors import red, cyan, green

class Server:
    def __init__(self, name, fs_tree):
        self.name = name
        self.tree = fs_tree
        self.cwd_path = []  # empty = root

    def _resolve(self, path_parts):
        node = self.tree["/"]
        for p in path_parts:
            if isinstance(node, dict) and p in node: 
                node = node[p]
            else: 
                return None
        return node

    def pwd(self): 
        return '/' + '/'.join(self.cwd_path) if self.cwd_path else '/'

    def ls(self):
        node = self._resolve(self.cwd_path)
        if not isinstance(node, dict): 
            return red("Error: cannot list.")
        items = [cyan(n+'/') if isinstance(c, dict) else green(n) 
                for n, c in node.items()]
        return '  '.join(items) if items else '(empty)'

    def cd(self, target):
        if target == '..':
            if self.cwd_path: 
                self.cwd_path.pop()
            return ''
        node = self._resolve(self.cwd_path)
        if target not in node or not isinstance(node[target], dict):
            return red(f"cd: {target}: Not a directory")
        self.cwd_path.append(target)
        return ''

    def cat(self, fname):
        node = self._resolve(self.cwd_path)
        if fname not in node: 
            return red(f"cat: {fname}: No such file")
        if isinstance(node[fname], dict): 
            return red(f"cat: {fname}: Is a directory")
        return node[fname]

    def reset_path(self): 
        self.cwd_path = []