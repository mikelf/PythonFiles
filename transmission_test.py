import transmissionrpc
def clearTrans():
	tc = transmissionrpc.Client('server', port=8081,user='user', password='pasword')
	sesion = tc.get_session()
	dowloaddir = sesion.download_dir
	print("------------------------------------------------------------------")
	print("Removing finished torrents from :" + dowloaddir +"directory.")
	for torrent in tc.get_torrents():
		print (torrent.status)
		if torrent.status == "seeding":
			if torrent.name == "":
				print ("------files-----")
				tdata= torrent.files()
				print  (tdata[0]["name"].encode('iso-8859-1'))
	finished_ids = [t.id for t in tc.get_torrents() if t.percentDone == 1.0]
	if finished_ids:
		print (finished_ids)
		tc.remove_torrent(ids=finished_ids)
