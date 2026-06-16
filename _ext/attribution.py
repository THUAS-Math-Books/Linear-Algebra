def add_attribution(app, docname, source):
    """Add attribution at the top of the document."""
    
    # add an admonition at the top of the document, assuming markdown
    # check if the source is a md file:
    file_type = app.env.doc2path(docname).split('.')[-1]
    if file_type == 'md':
        str_list = ["```{admonition} This page originates from:",
                    ":class: attribution, margin",
                    "Hensbergen, A., & Verhulst, N. (2025). _Linear Algebra - 2nd edition_. TU Delft OPEN Books. [https://doi.org/10.59490/mt.241](https://doi.org/10.59490/mt.241)",
                    "```",""]
        str = "\n".join(str_list)
        source[0] = str + source[0]

def setup(app):
    
    app.connect('source-read', add_attribution)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }