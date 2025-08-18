{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1d3b10db-4df9-4d02-924c-35752585d239",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "# from dotenv import load_dotenv\n",
    "from typing import Optional\n",
    "\n",
    "# This line loads the .env file\n",
    "# load_dotenv()\n",
    "\n",
    "def get_key(name: str, default: Optional[str] = None) -> Optional[str]:\n",
    "    return os.getenv(name, default)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44b98140-c7eb-42b0-a52f-fe8357ce1639",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python(fe-course_env)",
   "language": "python",
   "name": "fe-course"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
