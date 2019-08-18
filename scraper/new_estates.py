from scraper.helpers import log
import smtplib

_new_estates = []


def new_estates_add(estate):
    _new_estates.append(estate)


def new_estates_handle():
    global _new_estates

    if len(_new_estates) > 0:
        print(f"Found {len(_new_estates)} new houses.")

        new_estates_count = len(_new_estates)
        message = f'Nalezeno {new_estates_count} novych domu.'

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com')
            server.login('sevcik.mi@gmail.com', 'iischbndcqtqeumy')
            server.sendmail(
                "sevcik.mi@gmail.com",
                "sevcik.mi@vodafonemail.cz",
                message
            )
            server.quit()
        except smtplib.SMTPAuthenticationError:
            print("Error authenticating to SMTP server.")
        except Exception as e:
            print(f"Unhandled error when sending email through SMTP: {str(e)}.")

    _new_estates = []
