{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPuZAjasKV/BPSYAHh2osO4",
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
        "<a href=\"https://colab.research.google.com/github/iamiratsh/amir-hossein-atashkar/blob/main/Class%20circle.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "{\n",
        "  \"nbformat\": 4,\n",
        "  \"nbformat_minor\": 0,\n",
        "  \"metadata\": {\n",
        "    \"colab\": {\n",
        "      \"provenance\": [],\n",
        "      \"authorship_tag\": \"ABX9TyNhkkSPgJQp2QCDA1O/gMrF\",\n",
        "      \"include_colab_link\": true\n",
        "    },\n",
        "    \"kernelspec\": {\n",
        "      \"name\": \"python3\",\n",
        "      \"display_name\": \"Python 3\"\n",
        "    },\n",
        "    \"language_info\": {\n",
        "      \"name\": \"python\"\n",
        "    }\n",
        "  },\n",
        "  \"cells\": [\n",
        "    {\n",
        "      \"cell_type\": \"markdown\",\n",
        "      \"metadata\": {\n",
        "        \"id\": \"view-in-github\",\n",
        "        \"colab_type\": \"text\"\n",
        "      },\n",
        "      \"source\": [\n",
        "        \"<a href=\\\"https://colab.research.google.com/github/Whyoblomovisme/barname-nevisi/blob/main/Class%20circle.py\\\" target=\\\"_parent\\\"><img src=\\\"https://colab.research.google.com/assets/colab-badge.svg\\\" alt=\\\"Open In Colab\\\"/></a>\"\n",
        "      ]\n",
        "    },\n",
        "    {\n",
        "      \"cell_type\": \"markdown\",\n",
        "      \"source\": [],\n",
        "      \"metadata\": {\n",
        "        \"id\": \"OFQSfNtApWFd\"\n",
        "      }\n",
        "    },\n",
        "    {\n",
        "      \"cell_type\": \"code\",\n",
        "      \"source\": [\n",
        "        \"\\n\",\n",
        "        \"import math\\n\",\n",
        "        \"class circle():\\n\",\n",
        "        \"    pi=math.pi\\n\",\n",
        "        \"    def __init__ (self, r=5):\\n\",\n",
        "        \"        self.rad = r\\n\",\n",
        "        \"        print(\\\"circle created\\\")\\n\",\n",
        "        \"    def perim(self):\\n\",\n",
        "        \"        return 2*pi*self.rad\\n\",\n",
        "        \"    def Area(self):\\n\",\n",
        "        \"        return p*r*r\\n\",\n",
        "        \"    def __del__ (self):\\n\",\n",
        "        \"        print(\\\"circle deleted\\\")\\n\",\n",
        "        \"        return -1\\n\",\n",
        "        \"K = circle(10) #یک آبجکت به اندازه 10 وارد کلاس دایره میکند\\n\",\n",
        "        \"print(K.Area)\\n\",\n",
        "        \"print(K.perim)\\n\",\n",
        "        \"print(K.pi)\\n\",\n",
        "        \"del K\\n\",\n",
        "        \"#circle created\\n\",\n",
        "        \"#314\\n\",\n",
        "        \"#62.8\\n\",\n",
        "        \"#3.14\\n\",\n",
        "        \"#circle deleted\"\n",
        "      ],\n",
        "      \"metadata\": {\n",
        "        \"id\": \"KcFTLCmSD5ps\",\n",
        "        \"colab\": {\n",
        "          \"base_uri\": \"https://localhost:8080/\"\n",
        "        },\n",
        "        \"outputId\": \"b6070a8d-a53c-4938-bd67-6052b079c73c\"\n",
        "      },\n",
        "      \"execution_count\": null,\n",
        "      \"outputs\": [\n",
        "        {\n",
        "          \"output_type\": \"stream\",\n",
        "          \"name\": \"stdout\",\n",
        "          \"text\": [\n",
        "            \"circle created\\n\",\n",
        "            \"<bound method circle.Area of <__main__.circle object at 0x7a4d027390f0>>\\n\",\n",
        "            \"<bound method circle.perim of <__main__.circle object at 0x7a4d027390f0>>\\n\",\n",
        "            \"3.141592653589793\\n\",\n",
        "            \"circle deleted\\n\"\n",
        "          ]\n",
        "        }\n",
        "      ]\n",
        "    }\n",
        "  ]\n",
        "}"
      ],
      "metadata": {
        "id": "ruJJTSw7W_pS"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}