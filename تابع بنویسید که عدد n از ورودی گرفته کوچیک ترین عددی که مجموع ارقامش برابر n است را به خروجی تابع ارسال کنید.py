{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPARfhCz9IGMK4l5twRoqup",
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
        "<a href=\"https://colab.research.google.com/github/iamiratsh/amir-hossein-atashkar/blob/main/%D8%AA%D8%A7%D8%A8%D8%B9%20%D8%A8%D9%86%D9%88%DB%8C%D8%B3%DB%8C%D8%AF%20%DA%A9%D9%87%20%D8%B9%D8%AF%D8%AF%20n%20%D8%A7%D8%B2%20%D9%88%D8%B1%D9%88%D8%AF%DB%8C%20%DA%AF%D8%B1%D9%81%D8%AA%D9%87%20%DA%A9%D9%88%DA%86%DB%8C%DA%A9%20%D8%AA%D8%B1%DB%8C%D9%86%20%D8%B9%D8%AF%D8%AF%DB%8C%20%DA%A9%D9%87%20%D9%85%D8%AC%D9%85%D9%88%D8%B9%20%D8%A7%D8%B1%D9%82%D8%A7%D9%85%D8%B4%20%D8%A8%D8%B1%D8%A7%D8%A8%D8%B1%20n%20%D8%A7%D8%B3%D8%AA%20%D8%B1%D8%A7%20%D8%A8%D9%87%20%D8%AE%D8%B1%D9%88%D8%AC%DB%8C%20%D8%AA%D8%A7%D8%A8%D8%B9%20%D8%A7%D8%B1%D8%B3%D8%A7%D9%84%20%DA%A9%D9%86%DB%8C%D8%AF.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#تابع بنویسید که عدد n از ورودی گرفته کوچیک ترین عددی که مجموع ارقامش برابر n است را به خروجی تابع ارسال کنید\n",
        "def majmoe(t):\n",
        "    ssum = 0\n",
        "    while t!= 0:\n",
        "        ssum += t%10\n",
        "        t //= 10\n",
        "    return ssum\n",
        "def function1(n):\n",
        "    for i in range(n):\n",
        "      K = majmoe(i)\n",
        "      if K == n:\n",
        "       return K\n",
        "    return print('not found')"
      ],
      "metadata": {
        "id": "K64Xi_mU5Gez"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}