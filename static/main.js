let COLUMN = document.getElementById('column').value,
	TYPE = document.getElementById('condition').value,
	VALUE = document.getElementById('filter-val').value;

$(function () {

	$.get('/api/filter-table/').done(function (data) {
		if (data['count'] > 0) {
			generateTable(data);
		}
	});

	function generateTable(data) {
		let row = ''
		for (let key in data['results']) {
			row += `<tr>
				<td>${data['results'][key]['date']}</td>
				<td>${data['results'][key]['name']}</td>
				<td>${data['results'][key]['count']}</td>
				<td>${data['results'][key]['distance']}</td>
			</tr>`
		}

		if (data['next']) {
			$('#nextPage a').attr('data-url', data['next']);
		} else
			$('#nextPage a').removeAttr('data-url');
		if (data['previous']) {
			$('#prevPage a').attr('data-url', data['previous']);
		} else
			$('#prevPage a').removeAttr('data-url');

		$('#table-datas').html(row);
	}

	function get_another_page(url) {
		$.get(url).done(function (data) {
			if (data['count'] > 0) {
				generateTable(data);
			}
		});
	}

	$('.page-step a').on('click', function () {
		let url = $(this).attr('data-url')
		get_another_page(url);
	});


	$('#column').change(function () {
		if (this.value === 'name') {
			$('#filter-val').attr('type', 'text')
		} else {
			$('#filter-val').attr('type', 'number')
		}
	});


	$('#filtrate').on('click', function () {
		COLUMN = document.getElementById('column').value;
		TYPE = document.getElementById('condition').value;
		VALUE = document.getElementById('filter-val').value;

		let url = `api/filter-table/?column=${COLUMN}&condition=${TYPE}&value=${VALUE}`
		console.log(url)
		$.get(url).done(function (data) {
			console.log(data)
			generateTable(data)
		});
	});

});