{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOeYqmkeRCypAitgKmzeY4D",
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
        "<a href=\"https://colab.research.google.com/github/iamiratsh/amir-hossein-atashkar/blob/main/%23%DA%A9%D8%AF%20%D9%86%D9%87%D8%A7%DB%8C%DB%8C%20%DA%A9%20%D9%85%20%D9%85.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#کد نهایی ک م م\n",
        "def lcm(x, y):\n",
        "   if x > y:\n",
        "       lcm_ = x\n",
        "   else:\n",
        "       lcm_ = y\n",
        "\n",
        "   while(True):\n",
        "       if((lcm_ % x == 0) and (lcm_ % y == 0)):\n",
        "           break\n",
        "       lcm_ += 1\n",
        "\n",
        "   return lcm_\n",
        "\n",
        "\n",
        "num1 = int(input())\n",
        "num2 = int(input())\n",
        "print(\"lcm: \", lcm(num1, num2))"
      ],
      "metadata": {
        "id": "TrXRlG2KQqqU"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}