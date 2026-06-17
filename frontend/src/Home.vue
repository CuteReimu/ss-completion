<template>
  <el-alert title="感谢计时器生成器交流群的群友们热心提供存档，协助开发。代码仓库：https://github.com/CuteReimu/ss-completion" type="info" effect="dark" close-text="前往" @close="openGithub"></el-alert>
  <el-upload drag accept=".dat" :auto-upload="false" :show-file-list="false" :on-change="onUploadFile">
    <el-icon class="el-icon--upload"><upload-filled style="width: 80px;"></upload-filled></el-icon>
    <div class="el-upload__text">
      你可以将存档文件拖拽到这里或者 <em>点击上传</em>
    </div>
  </el-upload>
  <div class="btn-container">
    <el-button @click="OpenDataFolder" type="primary">点击打开存档目录</el-button>
    <el-button @click="RefreshAnalyze" type="primary" :disabled="disableReloadBtn">重新解析存档</el-button>
    <el-button @click="OutputResult" type="primary" :disabled="disableReloadBtn">导出解析后的存档</el-button>
    <el-button @click="ModifyAnalyzeScript" type="primary">修改解析脚本</el-button>
  </div>
  <el-text size="large" style="margin: 10px 0;">完成度：{{data.Completion ?? 0}}%</el-text>
  <div class="card-container">
    <el-card v-for="category in data.Categories">
      <template #header>{{category.name}}</template>
      <el-table :show-header="false" border :data="category.items" :row-class-name="determineRowClass" @row-click="goToWiki">
        <el-table-column label="名称">
          <template #default="scope">
            <el-tooltip effect="dark" v-if="scope.row.desc" :content="scope.row.desc" placement="left">
              <div><el-image v-if="scope.row.icon" :src="scope.row.icon" fit="scale-down" />{{scope.row.show_text}}</div>
            </el-tooltip>
            <div v-else><el-image v-if="scope.row.icon" :src="scope.row.icon" fit="scale-down" />{{scope.row.show_text}}</div>
          </template>
        </el-table-column>
        <el-table-column prop="status_text" label="状态" width="80">
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import {
  ElAlert, ElText, ElUpload, ElIcon, ElTable, ElTableColumn,
  ElButton, UploadFile, ElMessage, ElCard, ElTooltip, ElImage,
} from 'element-plus';
import { UploadFilled } from '@element-plus/icons-vue';
import { BrowserOpenURL, LogError } from '../wailsjs/runtime';
import { OpenDataFolder, DecryptFile, ReDecryptFile, SaveBuf, ModifyScript } from '../wailsjs/go/main/App';
import { main } from "../wailsjs/go/models";

const disableReloadBtn = ref(true);
const data = ref<main.AnalyzeResult>(new main.AnalyzeResult());

function determineRowClass({row}) {
  let c = '';
  switch (row.status) {
    case 2: c = 'success-row'; break;
    case 1: c = 'warning-row'; break;
    default: c = 'danger-row'; break;
  }
  if (row.wiki) c += " clickable-row";
  return c;
}

function onUploadFile(file: UploadFile) {
  if (!file?.raw) return;
  file.raw.text().then(text => {
    DecryptFile(text).then(res => {
      data.value = res;
      disableReloadBtn.value = false;
      ElMessage({ message: "解析成功", type: 'success', plain: true });
    }).catch(err => {
      LogError(err);
      ElMessage({ message: String(err), type: 'error', plain: true });
    })
  }).catch(e => {
    LogError(e);
    ElMessage({ message: String(e), type: 'error', plain: true });
  });
}

function RefreshAnalyze() {
  ReDecryptFile().then(res => {
    data.value = res;
    ElMessage({ message: "解析成功", type: 'success', plain: true });
  }).catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  })
}

function OutputResult() {
  SaveBuf().catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  })
}

function ModifyAnalyzeScript() {
  ModifyScript().catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  })
}

function openGithub() {
  BrowserOpenURL('https://github.com/CuteReimu/ss-completion');
}

function goToWiki(row: main.ItemResult) {
  if (row.wiki) BrowserOpenURL(row.wiki);
}
</script>
