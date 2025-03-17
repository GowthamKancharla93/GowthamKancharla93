{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNsdBrXJzu9T0koWTt1NgRL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/GowthamKancharla93/GowthamKancharla93/blob/main/Webscraping.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "import smtplib\n",
        "from email.mime.text import MIMEText\n",
        "import time\n",
        "import re\n",
        "\n",
        "def get_price(url):\n",
        "    try:\n",
        "        response = requests.get(url, headers={\n",
        "            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',\n",
        "            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',\n",
        "            'Accept-Language': 'en-US,en;q=0.9',\n",
        "            'Accept-Encoding': 'gzip, deflate, br',\n",
        "            'Connection': 'keep-alive',\n",
        "            'DNT': '1',\n",
        "            'Cache-Control': 'max-age=0',\n",
        "            'Upgrade-Insecure-Requests': '1',\n",
        "            'Sec-Fetch-Dest': 'document',\n",
        "            'Sec-Fetch-Mode': 'navigate',\n",
        "            'Sec-Fetch-Site': 'none',\n",
        "            'Sec-Fetch-User': '?1'\n",
        "        })\n",
        "\n",
        "        soup = BeautifulSoup(response.content, 'html.parser')\n",
        "        price_element = soup.select_one('.a-price-whole')\n",
        "\n",
        "        if price_element:\n",
        "            price_text = price_element.text.strip()\n",
        "            price_numbers = re.findall(r'[\\d]+', price_text)\n",
        "            if price_numbers:\n",
        "                price = float(price_numbers[0].replace(',', ''))\n",
        "                return price\n",
        "            else:\n",
        "                return None\n",
        "        return None\n",
        "\n",
        "    except Exception as e:\n",
        "        print(e)\n",
        "        return None\n",
        "\n",
        "def send_email(subject, body, to_email):\n",
        "    gmail_user = 'gowthamkancharla225@gmail.com'\n",
        "    gmail_password = '9347441337'\n",
        "\n",
        "    msg = MIMEText(body)\n",
        "    msg['From'] = gmail_user\n",
        "    msg['To'] = to_email\n",
        "    msg['Subject'] = subject\n",
        "\n",
        "    try:\n",
        "        server = smtplib.SMTP('smtp.gmail.com', 587)\n",
        "        server.starttls()\n",
        "        server.login(gmail_user, gmail_password)\n",
        "        server.sendmail(gmail_user, to_email, msg.as_string())\n",
        "        server.quit()\n",
        "        print(\"Email sent successfully\")\n",
        "    except Exception as e:\n",
        "        print(\"Error sending email:\", e)\n",
        "\n",
        "def track_price(url, target_price, check_interval=3600):\n",
        "    while True:\n",
        "        current_price = get_price(url)\n",
        "        print(f'Current Price: {current_price}')\n",
        "\n",
        "        if current_price is not None and current_price <= target_price:\n",
        "            subject = \"Price Dropped! Check it Out!\"\n",
        "            body = f\"\"\"\n",
        "            The price dropped to {current_price}!\n",
        "            This is less than your target price of {target_price}.\n",
        "            Check the product here: {url}\n",
        "            \"\"\"\n",
        "            send_email(subject, body, 'gowthamchoudary63@gmail.com')\n",
        "            print('Email sent. Stopping tracking.')\n",
        "            break\n",
        "        else:\n",
        "            print('Price not dropped yet, checking again in 1 hour...')\n",
        "            time.sleep(check_interval)\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    url =\"https://www.amazon.in/MSI-i5-12450H-Windows-GeForce-B12UC-2241IN/dp/B0DQPV4C8Q/ref=sr_1_2?crid=30V2JKA0GA1FD&dib=eyJ2IjoiMSJ9.OcCyCFb3nfHmrfaXi4rWv4Riu_asQPHtolgnmNQNmCfl0AbpKnUYh-M7Doh7cpvVI_T2eSNN4aoi74OCgl0G6wzJltALicVH-ja7SZbTuUHDexnBAHt223mTEvdCZrzE8Z3fVaDXaxV27ZSMFwcz6PJdzE0W7Jz9JA2sjYmNHxKNBsIizn7zvbVQbxqG2ejIxQ2EcnGoGbSIsKXMNopOfV6kyef6xx5ZZ025vsgptS8.dXq2cV5DUjAbzAIwT0F_VTUG0AusnDucFObuYlcHx-E&dib_tag=se&keywords=msi+cyborg+15+intel+core+i5+12th+gen+12450h&nsdOptOutParam=true&qid=1742232435&sprefix=Msi+cyborg+15+intel+i5+12%2Caps%2C268&sr=8-2\"\n",
        "    target_price = 57999\n",
        "    track_price(url, target_price)\n",
        "    print(\"Price tracking started\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 473
        },
        "id": "f7lGP32X-paA",
        "outputId": "675945cd-3a01-42a5-c305-5a71c84a477f"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Current Price: None\n",
            "Price not dropped yet, checking again in 2 hours...\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-10-46fcfe108b0e>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     81\u001b[0m     \u001b[0murl\u001b[0m \u001b[0;34m=\u001b[0m\u001b[0;34m\"https://www.amazon.in/MSI-i5-12450H-Windows-GeForce-B12UC-2241IN/dp/B0DQPV4C8Q/ref=sr_1_2?crid=30V2JKA0GA1FD&dib=eyJ2IjoiMSJ9.OcCyCFb3nfHmrfaXi4rWv4Riu_asQPHtolgnmNQNmCfl0AbpKnUYh-M7Doh7cpvVI_T2eSNN4aoi74OCgl0G6wzJltALicVH-ja7SZbTuUHDexnBAHt223mTEvdCZrzE8Z3fVaDXaxV27ZSMFwcz6PJdzE0W7Jz9JA2sjYmNHxKNBsIizn7zvbVQbxqG2ejIxQ2EcnGoGbSIsKXMNopOfV6kyef6xx5ZZ025vsgptS8.dXq2cV5DUjAbzAIwT0F_VTUG0AusnDucFObuYlcHx-E&dib_tag=se&keywords=msi+cyborg+15+intel+core+i5+12th+gen+12450h&nsdOptOutParam=true&qid=1742232435&sprefix=Msi+cyborg+15+intel+i5+12%2Caps%2C268&sr=8-2\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     82\u001b[0m     \u001b[0mtarget_price\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m57999\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 83\u001b[0;31m     \u001b[0mtrack_price\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtarget_price\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     84\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Price tracking started\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-10-46fcfe108b0e>\u001b[0m in \u001b[0;36mtrack_price\u001b[0;34m(url, target_price, check_interval)\u001b[0m\n\u001b[1;32m     76\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     77\u001b[0m             \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Price not dropped yet, checking again in 2 hours...'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 78\u001b[0;31m             \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcheck_interval\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     79\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     80\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'__main__'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    }
  ]
}