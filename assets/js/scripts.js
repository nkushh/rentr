function format_date(date_info){
	const formattedDate = new Date(date_info)
		.toLocaleString('en-us', {
			month: 'long',
			day: 'numeric',
			year: 'numeric',
			hour: 'numeric',
			minute: '2-digit',
			hour12: true,
		})
		.replace('AM', 'a.m.')
		.replace('PM', 'p.m.');

	return formattedDate;
}