{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNNbFNcEe7halpf97iDm11z",
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
        "<a href=\"https://colab.research.google.com/github/iamiratsh/amir-hossein-atashkar/blob/main/%D8%AA%D8%A7%D8%A8%D8%B9%20%D8%A8%D9%86%D9%88%DB%8C%D8%B3%DB%8C%D8%AF%20%D8%B9%D8%AF%D8%AF%20%D8%B5%D8%AD%DB%8C%D8%AD%20%D8%A7%D8%B2%20%D9%88%D8%B1%D9%88%D8%AF%DB%8C%20%DA%AF%D8%B1%D9%81%D8%AA%D9%87%20%D8%B3%D9%BE%D8%B3%20%D8%AA%D9%85%D8%A7%D9%85%DB%8C%20%D8%A7%D8%B9%D8%AF%D8%A7%D8%AF%20%DA%A9%D9%88%DA%86%DB%8C%DA%A9%20%D8%AA%D8%B1%20n%20%DA%A9%D9%87%20%D9%81%D9%82%D8%B7%20%D8%B4%D8%A7%D9%85%D9%84%202%20%D9%88%205%20%D9%85%DB%8C%20%D8%A8%D8%A7%D8%B4%D8%AF%20%D8%AF%D8%B1%20%D9%88%D8%B1%D9%88%D8%AF%DB%8C%20%DA%86%D8%A7%D9%BE%20%DA%A9%D9%86%D8%AF.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#تابع بنویسید عدد صحیح از ورودی گرفته سپس تمامی اعداد کوچیک تر n که فقط شامل 2 و 5 می باشد در ورودی چاپ کند\n",
        "\n",
        "def shamel2v5(L):\n",
        "    while L!=0:\n",
        "        k=L%10\n",
        "        if k!=2 and k!=5:\n",
        "          return False\n",
        "        L//=10\n",
        "    return True\n",
        "def function2(n):\n",
        "    for i in range(n):\n",
        "      K = shamel2v5(i)\n",
        "      if K:\n",
        "       Print(i)"
      ],
      "metadata": {
        "id": "9yid503b8HY9"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}