
# build images
docker build --target base-backend -t sd_backend_img ./backend
docker build --target test-backend -t sd_backend_test_img ./backend


# run tests (pytest) (workdir: /backend)
docker run sd_backend_test_img




# # debug
# docker run -it -w "/backend" sd_backend_img sh
# run server (workdir: /backend/src)
# docker run --rm -p 8000:8000 --name sd_backend sd_backend_img