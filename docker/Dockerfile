FROM python:3.8
WORKDIR /workspace/tdx-tools
RUN mkdir /tmp/tdx-tools \
    && cp -r ../../tdx-tools/* /tmp/tdx-tools/
COPY /tmp/tdx-tools/ /workspace/tdx-tools
RUN ls /workspace/tdx-tools
# RUN ./install_editable.sh
# CMD ["tdx-main"]
