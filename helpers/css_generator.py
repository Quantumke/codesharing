from pygments import formatters, styles
style = styles.get_style_by_name('murphy')
formatter = formatters.HtmlFormatter(style=style)
outfile = open('pygments.css', 'w')
outfile.write(formatters.get_style_defs())
outfile.close()
