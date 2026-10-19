import pathlib, sys
here = pathlib.Path(__file__).parent   # tools/tree-pages: the two page templates and the code they share
viz = pathlib.Path(sys.argv[1])
data = (viz / 'tools/tree-overfit-data.json').read_text()
common = (here / 'tree-common.js').read_text().replace('__DATA__', data)
head = (here / 'shell-head.html').read_text()
for src, dst, title in [('overfit.html', 'ch5/overfitting.html', 'Overfitting'), ('limit.html', 'ch5/limiting-the-tree.html', 'Limiting the Tree')]:
    p = here / src
    if not p.exists(): continue
    (viz / dst).write_text(p.read_text().replace('__HEAD__', head.replace('__TITLE__', title)).replace('__COMMON__', common))
    print('wrote', dst)
