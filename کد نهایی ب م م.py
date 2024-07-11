{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyODmcON0nMBTc/n3xhdr5Gq",
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
        "<a href=\"https://colab.research.google.com/github/iamiratsh/amir-hossein-atashkar/blob/main/%DA%A9%D8%AF%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C%20%D8%A8%20%D9%85%20%D9%85.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#کد نهایی ب م م\n",
        "def gcd(x, y):\n",
        "   if x > y:\n",
        "       gcd_ = x\n",
        "   else:\n",
        "       gcd_ = y\n",
        "\n",
        "   while(True):\n",
        "       if((x % gcd_ == 0) and (y % gcd_ == 0)):\n",
        "           break\n",
        "       gcd_ -= 1\n",
        "\n",
        "   return gcd_\n",
        "\n",
        "\n",
        "num1 = int(input())\n",
        "num2 = int(input())\n",
        "print(\"gcd: \", gcd(num1, num2))"
      ],
      "metadata": {
        "id": "PhmUi55W6W2_"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}