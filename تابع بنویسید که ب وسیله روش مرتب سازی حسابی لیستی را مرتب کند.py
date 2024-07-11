{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMJQrBfYshIHGj/r1vQCOsj",
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
        "<a href=\"https://colab.research.google.com/github/iamiratsh/amir-hossein-atashkar/blob/main/%D8%AA%D8%A7%D8%A8%D8%B9%20%D8%A8%D9%86%D9%88%DB%8C%D8%B3%DB%8C%D8%AF%20%DA%A9%D9%87%20%D8%A8%20%D9%88%D8%B3%DB%8C%D9%84%D9%87%20%D8%B1%D9%88%D8%B4%20%D9%85%D8%B1%D8%AA%D8%A8%20%D8%B3%D8%A7%D8%B2%DB%8C%20%D8%AD%D8%B3%D8%A7%D8%A8%DB%8C%20%D9%84%DB%8C%D8%B3%D8%AA%DB%8C%20%D8%B1%D8%A7%20%D9%85%D8%B1%D8%AA%D8%A8%20%DA%A9%D9%86%D8%AF.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#تابع بنویسید که ب وسیله روش مرتب سازی حسابی لیستی را مرتب کند\n",
        "def b_sort(k=[] ,s=10):\n",
        "    if k is not None:\n",
        "        for i in range(s,1):\n",
        "            for j in range(s,1,i):\n",
        "                if k[j]>k[j+1]:\n",
        "                    temp = k[j]\n",
        "                    k[j] = k[j +1]\n",
        "                    k[j + 1] = temp"
      ],
      "metadata": {
        "id": "pbhZ9dH58iOF"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}