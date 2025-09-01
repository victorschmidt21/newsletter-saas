from textwrap import dedent

def render_email(articles):
    ideias_email = ""
    for article in articles:
        ideias_email += f"""
        <div class="idea">
          <div class="idea-title">{article.title}</div>
          <p class="idea-desc">{article.description}</p>
        </div>
        """

    template = f"""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Ideias de SaaS da Semana</title>
        <style media="all" type="text/css">
          body {{
            font-family: Helvetica, sans-serif;
            -webkit-font-smoothing: antialiased;
            font-size: 16px;
            line-height: 1.4;
            background-color: #f4f5f6;
            margin: 0;
            padding: 0;
          }}
          .container {{
            margin: 0 auto;
            max-width: 600px;
            padding: 24px;
          }}
          .main {{
            background: #ffffff;
            border: 1px solid #eaebed;
            border-radius: 16px;
            width: 100%;
          }}
          .wrapper {{
            padding: 24px;
          }}
          .idea {{
            border: 1px solid #eaebed;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 16px;
            background: #fafafa;
          }}
          .idea-title {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #0867ec;
          }}
          .idea-desc {{
            font-size: 15px;
            margin-bottom: 8px;
            color: #333;
          }}
          .idea-reason {{
            font-size: 14px;
            color: #555;
          }}
          .btn-primary a {{
            background-color: #0867ec;
            border-radius: 6px;
            color: #fff;
            padding: 12px 24px;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
          }}
          .footer {{
            text-align: center;
            color: #9a9ea6;
            font-size: 14px;
            margin-top: 24px;
          }}
          .social-links a {{
            margin: 0 8px;
            text-decoration: none;
            color: #0867ec;
            font-weight: bold;
          }}
          @media only screen and (max-width: 640px) {{
            .container {{
              width: 100% !important;
              padding: 12px !important;
            }}
            .wrapper {{
              padding: 12px !important;
            }}
          }}
        </style>
      </head>
      <body>
        <div class="container">
          <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="main">
            <tr>
              <td class="wrapper">
                {ideias_email}

                <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary" style="margin-top: 20px">
                  <tr>
                    <td align="center">
                      <a href="http://seusite.com" target="_blank">Ver todas as ideias</a>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>

          <div class="footer">
            <p>Desenvolvido por <strong>Victor Schmidt</strong></p>
            <div class="social-links">
              <a href="https://www.linkedin.com/in/victor-schmidt-329827300/" target="_blank">LinkedIn</a> |
              <a href="https://www.instagram.com/victorschmidt21/" target="_blank">Instagram</a> |
              <a href="https://github.com/victorschmidt21" target="_blank">GitHub</a>
            </div>
            <p style="margin-top: 12px; font-size: 12px; color: #bbb">
              Você recebeu este email porque está inscrito na nossa newsletter.<br />
              <a href="#" style="color: #9a9ea6; text-decoration: underline">Descadastrar</a>
            </p>
          </div>
        </div>
      </body>
    </html>
    """
    return dedent(template)

def getTemplate(articles):
    return render_email(articles)
