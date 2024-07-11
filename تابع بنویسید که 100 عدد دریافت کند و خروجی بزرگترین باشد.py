{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPEPe4s3vbhhTIkArCOHy37",
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
        "<a href=\"https://colab.research.google.com/github/iamiratsh/amir-hossein-atashkar/blob/main/%D8%AA%D8%A7%D8%A8%D8%B9%20%D8%A8%D9%86%D9%88%DB%8C%D8%B3%DB%8C%D8%AF%20%DA%A9%D9%87%20100%20%D8%B9%D8%AF%D8%AF%20%D8%AF%D8%B1%DB%8C%D8%A7%D9%81%D8%AA%20%DA%A9%D9%86%D8%AF%20%D9%88%20%D8%AE%D8%B1%D9%88%D8%AC%DB%8C%20%D8%A8%D8%B2%D8%B1%DA%AF%D8%AA%D8%B1%DB%8C%D9%86%20%D8%A8%D8%A7%D8%B4%D8%AF.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#تابع بنویسید که 100 عدد دریافت کند و خروجی بزرگترین باشد\n",
        "def max100():\n",
        "    a=input()\n",
        "    a=int(a)\n",
        "    max=a\n",
        "    for i in rang (0,100):\n",
        "        a=int (input())\n",
        "        if a>max:\n",
        "             max=a\n",
        "        return max"
      ],
      "metadata": {
        "id": "d1_SYOX72OHZ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}