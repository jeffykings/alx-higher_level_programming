#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp, *first_half, *second_half;
	int len, n, half;

	len = 0;
	temp = *head;
	first_half = second_half = *head;
	if (*head == NULL)
		return (1);
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	half = len / 2;
	n = half - 1;
	if (half == 1)
	{
		if (len % 2 == 0)
			second_half = second_half->next;
		else
			second_half = second_half->next->next;
	} else
	{
		while (n)
		{
			first_half = first_half->next;
			if (len % 2 != 0 && (n > 1))
				second_half = second_half->next->next;
			else
			{
				if (n > 1)
					second_half = second_half->next;
			}
			n--;
		}
		second_half = second_half->next;
	}
	return (check(second_half, first_half, *head, half));
}

int check(listint_t *scnd_half, listint_t *first_hlf, listint_t *h, int half)
{
	listint_t *temp;
	int i;

	while (scnd_half)
	{
		temp = h;
		half--;
		if (scnd_half->n != first_hlf->n)
			return (0);
		for (i = 0; i < half; i++)
			temp = temp->next;
		first_hlf = temp;
		scnd_half = scnd_half->next;
	}
	return (1);
}
