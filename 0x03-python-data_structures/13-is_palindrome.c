#include "lists.h"

/**
 * is_palindrome - checks for palindrome
 * @head: header of the list
 * Return: 1 if true or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *first_half, *second_half;
	int len, n, half;

	len = 0;
	temp = *head;
	first_half = second_half = *head;
	if (*head == NULL || (*head)->next == NULL)
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
	return (check(second_half, first_half, *head, half, len));
}

/**
 * check - for palindrome
 * @snd_hlf: pointer that moves through the second half of the list
 * @ft_hlf: pointer that moves through the first half of the list
 * @h: head of the list
 * @hlf: integer half of the list
 * @ln: lenght of the list
 * Return: 1 for palindrome else 0
 */
int check(listint_t *snd_hlf, listint_t *ft_hlf, listint_t *h, int hlf, int ln)
{
	listint_t *temp;
	int i, n = 0;

	while (snd_hlf)
	{
		temp = h;
		hlf--;
		if (snd_hlf->n != ft_hlf->n)
			return (0);
		for (i = 0; i < hlf; i++)
		{
			temp = temp->next;
			if (ln % 2 != 0 && n < 1)
			{
				hlf--;
				n++;
			}
		}
		ft_hlf = temp;
		snd_hlf = snd_hlf->next;
	}
	return (1);
}
