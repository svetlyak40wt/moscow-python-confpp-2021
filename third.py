import io
import base64
import requests

def format_headers(headers):
    output = io.StringIO()
    output.write('<dl>')
    for key, value in sorted(headers.items()):
        output.write(f'<dt>{key}</dt>')
        output.write(f'<dd>{value}</dd>')
    output.write('</dl>')

    return output.getvalue()

def format_response(response):
    headers = response.headers
    content = response.content

    content_type = response.headers['content-type']

    if content_type == 'application/json':
        content = content.decode('utf-8')
        content = f'<pre><code>{content}</code></pre>'
    elif content_type.startswith('image/'):
        data = base64.b64encode(content).decode('ascii')
        content = f'<img src="data:{content_type};base64,{data}"/>'

    return f"""<h1>HTTP Response ({content_type})</h1>
               <table width="100%">
                 <tr style="vertical-align: top">
                   <td style="text-align: left; vertical-align: top;">
                     <h2>{response.status_code}</h2>
                     <h3>Headers</h3>
                     {format_headers(headers)}
                   </td>
                   <td style="text-align: left; vertical-align: top;">
                     <h3>Content</h3>
                     {content}
                   </td>
                  </tr>
                </table>
            """

def load_ipython_extension(ipython):
    print('Loading "requests rendered" extension')
    formatters = ipython.display_formatter.formatters
    formatter = formatters['text/html']
    formatter.for_type(requests.Response, format_response)

